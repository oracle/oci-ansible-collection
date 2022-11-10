# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import platform
import ansible
from ansible.module_utils import urls
import json
from ansible_collections.oracle.oci.plugins.module_utils import oci_version
import logging

try:
    import oci

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False

logger = logging.getLogger(__name__)


def get_oci_python_sdk_version():
    try:
        python_sdk_version = oci.__version__
    except AttributeError:
        python_sdk_version = None
    logger.debug("OCI-Python-Sdk version: {}".format(python_sdk_version))
    return python_sdk_version


def get_python_version():
    try:
        python_version = platform.python_version()
    except Exception:
        # didn't try any specific exception so that all kind of exceptions get caught here
        python_version = None
    logger.debug("Python Version: {}".format(python_version))
    return python_version


def get_ansible_version():
    try:
        ansible_version = ansible.__version__
    except AttributeError:
        ansible_version = None
    logger.debug("Ansible Version: {}".format(ansible_version))
    return ansible_version


def get_oci_ansible_collection_installed_version():
    try:
        oci_ansible_collection_version = oci_version.__version__
    except AttributeError:
        oci_ansible_collection_version = None
    logger.debug(
        "OCI-Ansible-Collections installed Version: {}".format(
            oci_ansible_collection_version
        )
    )
    return oci_ansible_collection_version


def get_oci_ansible_collection_latest_version():
    try:
        url = (
            "https://api.github.com/repos/oracle/oci-ansible-collection/releases/latest"
        )
        with urls.open_url(url) as req_response:
            req_response_json = json.loads(req_response.read())
            latest_version = req_response_json.get("name")
            if latest_version[0] == "v":
                latest_version = latest_version[1:]
    except Exception:
        latest_version = None

    logger.debug(
        "OCI-Ansible-Collections latest version available: {}".format(latest_version)
    )
    return latest_version


def get_oci_python_sdk_path():
    try:
        oci_python_sdk_path = oci.__path__
    except AttributeError:
        oci_python_sdk_path = None

    logger.debug("OCI-Python-Sdk path: {}".format(oci_python_sdk_path))
    return oci_python_sdk_path


def get_ansible_module_python_path():
    try:
        ansible_module_python_path = ansible.__path__
    except AttributeError:
        ansible_module_python_path = None

    logger.debug("Ansible module python path: {}".format(ansible_module_python_path))
    return ansible_module_python_path
