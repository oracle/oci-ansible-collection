# Copyright (c) 2020 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import inspect


def get_custom_class_mapping(modules):
    """Find the custom classes in the given modules and return a mapping with class name as key and class as value"""
    custom_class_mapping = {}
    for module in modules:
        for obj_name in dir(module):
            if not obj_name.endswith("Custom"):
                continue
            obj = getattr(module, obj_name)
            if inspect.isclass(obj):
                custom_class_mapping[obj_name] = obj
    return custom_class_mapping


# Due to the generalisations made about the resource APIs or because of the ease of use enhancements, the generated
# modules might not always be perfect. The custom behaviour is handled by having a custom class which is used to
# override the generated behaviour. Create a mapping of those custom classes so that we can dynamically override
# the behaviour.
# import the customisation files.
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_identity_custom_helpers,
    oci_network_custom_helpers,
    oci_compute_custom_helpers,
    oci_blockstorage_custom_helpers,
    oci_compute_management_custom_helpers,
    oci_audit_custom_helpers,
    oci_object_storage_custom_helpers,
    oci_key_management_custom_helpers,
    oci_file_storage_custom_helpers,
    oci_container_engine_custom_helpers,
    oci_load_balancer_custom_helpers,
    oci_database_custom_helpers,
    oci_streaming_custom_helpers,
    oci_functions_custom_helpers,
    oci_marketplace_custom_helpers,
    oci_dns_custom_helpers,
    oci_monitoring_custom_helpers,
    oci_ons_custom_helpers,
    oci_os_management_custom_helpers,
)  # noqa

custom_helper_mapping = get_custom_class_mapping(
    [
        oci_identity_custom_helpers,
        oci_network_custom_helpers,
        oci_compute_custom_helpers,
        oci_blockstorage_custom_helpers,
        oci_compute_management_custom_helpers,
        oci_audit_custom_helpers,
        oci_object_storage_custom_helpers,
        oci_key_management_custom_helpers,
        oci_file_storage_custom_helpers,
        oci_container_engine_custom_helpers,
        oci_load_balancer_custom_helpers,
        oci_database_custom_helpers,
        oci_streaming_custom_helpers,
        oci_functions_custom_helpers,
        oci_marketplace_custom_helpers,
        oci_dns_custom_helpers,
        oci_monitoring_custom_helpers,
        oci_ons_custom_helpers,
        oci_os_management_custom_helpers,
    ]
)
