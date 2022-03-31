# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
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
    oci_database_management_custom_helpers,
    oci_network_custom_helpers,
    oci_compute_custom_helpers,
    oci_blockstorage_custom_helpers,
    oci_compute_management_custom_helpers,
    oci_audit_custom_helpers,
    oci_object_storage_custom_helpers,
    oci_key_management_custom_helpers,
    oci_file_storage_custom_helpers,
    oci_container_engine_custom_helpers,
    oci_loadbalancer_custom_helpers,
    oci_database_custom_helpers,
    oci_streaming_custom_helpers,
    oci_functions_custom_helpers,
    oci_marketplace_custom_helpers,
    oci_dns_custom_helpers,
    oci_monitoring_custom_helpers,
    oci_ons_custom_helpers,
    oci_os_management_custom_helpers,
    oci_resource_manager_custom_helpers,
    oci_announcements_service_custom_helpers,
    oci_integration_custom_helpers,
    oci_nosql_custom_helpers,
    oci_apigateway_custom_helpers,
    oci_oce_custom_helpers,
    oci_waas_custom_helpers,
    oci_data_flow_custom_helpers,
    oci_analytics_custom_helpers,
    oci_data_science_custom_helpers,
    oci_database_tools_custom_helpers,
    oci_data_safe_custom_helpers,
    oci_data_catalog_custom_helpers,
    oci_data_connectivity_custom_helpers,
    oci_oda_custom_helpers,
    oci_mysql_custom_helpers,
    oci_bigdata_custom_helpers,
    oci_ocvp_custom_helpers,
    oci_logging_custom_helpers,
    oci_blockchain_customer_helpers,
    oci_log_analytics_custom_helpers,
    oci_cloud_guard_custom_helpers,
    oci_management_agent_custom_helpers,
    oci_compute_instance_agent_custom_helpers,
    oci_opsi_custom_helpers,
    oci_optimizer_custom_helpers,
    oci_management_dashboards_custom_helpers,
    oci_artifacts_custom_helpers,
    oci_network_load_balancer_custom_helpers,
    oci_service_catalog_custom_helpers,
    oci_golden_gate_custom_helpers,
    oci_generic_artifacts_content_custom_helpers,
    oci_database_migration_custom_helpers,
    oci_secrets_custom_helpers,
    oci_apm_control_plane_custom_helpers,
    oci_apm_synthetics_custom_helpers,
    oci_ai_anomaly_detection_custom_helpers,
    oci_usage_custom_helpers,
    oci_devops_custom_helpers,
    oci_certificates_management_custom_helpers,
    oci_budget_custom_helpers,
    oci_identity_data_plane_custom_helpers,
    oci_visual_builder_custom_helpers,
    oci_ai_vision_custom_helpers,
)  # noqa

custom_helper_mapping = get_custom_class_mapping(
    [
        oci_identity_custom_helpers,
        oci_database_management_custom_helpers,
        oci_network_custom_helpers,
        oci_compute_custom_helpers,
        oci_blockstorage_custom_helpers,
        oci_compute_management_custom_helpers,
        oci_audit_custom_helpers,
        oci_object_storage_custom_helpers,
        oci_key_management_custom_helpers,
        oci_data_connectivity_custom_helpers,
        oci_file_storage_custom_helpers,
        oci_container_engine_custom_helpers,
        oci_loadbalancer_custom_helpers,
        oci_database_custom_helpers,
        oci_streaming_custom_helpers,
        oci_functions_custom_helpers,
        oci_marketplace_custom_helpers,
        oci_dns_custom_helpers,
        oci_database_tools_custom_helpers,
        oci_monitoring_custom_helpers,
        oci_ons_custom_helpers,
        oci_os_management_custom_helpers,
        oci_resource_manager_custom_helpers,
        oci_announcements_service_custom_helpers,
        oci_integration_custom_helpers,
        oci_nosql_custom_helpers,
        oci_apigateway_custom_helpers,
        oci_oce_custom_helpers,
        oci_waas_custom_helpers,
        oci_data_flow_custom_helpers,
        oci_analytics_custom_helpers,
        oci_generic_artifacts_content_custom_helpers,
        oci_data_science_custom_helpers,
        oci_data_safe_custom_helpers,
        oci_data_catalog_custom_helpers,
        oci_oda_custom_helpers,
        oci_mysql_custom_helpers,
        oci_bigdata_custom_helpers,
        oci_ocvp_custom_helpers,
        oci_logging_custom_helpers,
        oci_blockchain_customer_helpers,
        oci_log_analytics_custom_helpers,
        oci_cloud_guard_custom_helpers,
        oci_management_agent_custom_helpers,
        oci_compute_instance_agent_custom_helpers,
        oci_opsi_custom_helpers,
        oci_optimizer_custom_helpers,
        oci_management_dashboards_custom_helpers,
        oci_artifacts_custom_helpers,
        oci_network_load_balancer_custom_helpers,
        oci_service_catalog_custom_helpers,
        oci_golden_gate_custom_helpers,
        oci_database_migration_custom_helpers,
        oci_secrets_custom_helpers,
        oci_apm_control_plane_custom_helpers,
        oci_apm_synthetics_custom_helpers,
        oci_ai_anomaly_detection_custom_helpers,
        oci_usage_custom_helpers,
        oci_devops_custom_helpers,
        oci_certificates_management_custom_helpers,
        oci_budget_custom_helpers,
        oci_identity_data_plane_custom_helpers,
        oci_visual_builder_custom_helpers,
        oci_ai_vision_custom_helpers,
    ]
)
