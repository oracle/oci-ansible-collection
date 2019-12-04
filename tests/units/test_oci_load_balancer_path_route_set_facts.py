# Copyright (c) 2018, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
import logging
from ansible.modules.cloud.oracle import oci_load_balancer_path_route_set_facts
from ansible.module_utils.oracle import oci_utils, oci_lb_utils

try:
    import oci
    from oci.util import to_dict
    from oci.load_balancer.models import (
        PathRoute,
        PathRouteSet,
        PathMatchType,
        WorkRequest,
    )
    from oci.exceptions import ServiceError, ClientError
except ImportError:
    raise SkipTest(
        "test_oci_load_balancer_path_route_set_facts.py requires `oci` module"
    )


class FakeModule(object):
    def __init__(self, **kwargs):
        self.params = kwargs

    def fail_json(self, *args, **kwargs):
        self.exit_args = args
        self.exit_kwargs = kwargs
        raise Exception(kwargs["msg"])

    def exit_json(self, *args, **kwargs):
        self.exit_args = args
        self.exit_kwargs = kwargs


@pytest.fixture()
def lb_client(mocker):
    mock_lb_client = mocker.patch(
        "oci.load_balancer.load_balancer_client.LoadBalancerClient"
    )
    return mock_lb_client.return_value


@pytest.fixture()
def oci_wait_until_patch(mocker):
    return mocker.patch.object(oci, "wait_until")


@pytest.fixture()
def list_all_resources_patch(mocker):
    return mocker.patch.object(oci_utils, "list_all_resources")


@pytest.fixture()
def oci_utils_call_with_backoff_patch(mocker):
    return mocker.patch.object(oci_utils, "call_with_backoff")


def setUpModule():
    logging.basicConfig(
        filename="/tmp/oci_ansible_module.log", filemode="a", level=logging.INFO
    )
    oci_load_balancer_path_route_set_facts.set_logger(logging)

    logging.basicConfig(
        filename="/tmp/oci_ansible_module.log", filemode="a", level=logging.INFO
    )
    oci_load_balancer_path_route_set_facts.set_logger(logging)


def test_list_load_balancer_path_route_sets_specific_path_route_set(
    lb_client, oci_utils_call_with_backoff_patch
):
    module = get_module(
        dict(
            {
                "path_route_set_name": "path_route_set1",
                "load_balancer_id": "ocid1.lodbalancer.xcds",
            }
        )
    )
    path_route_set = create_default_path_route_set()
    lb_client.get_path_route_set.return_value = get_response(
        200, None, path_route_set, None
    )
    oci_utils_call_with_backoff_patch.return_value = get_response(
        200, None, path_route_set, None
    )
    result = oci_load_balancer_path_route_set_facts.list_load_balancer_path_route_sets(
        lb_client, module
    )
    assert result["path_route_sets"][0]["name"] is path_route_set.name


def test_list_load_balancer_path_routes_all_path_routes(
    lb_client, list_all_resources_patch
):
    module = get_module(dict({"load_balancer_id": "ocid1.lodbalancer.xcds"}))
    path_route_set = create_default_path_route_set()
    list_all_resources_patch.return_value = [path_route_set]
    result = oci_load_balancer_path_route_set_facts.list_load_balancer_path_route_sets(
        lb_client, module
    )
    assert result["path_route_sets"][0]["name"] is path_route_set.name


def test_list_load_balancer_path_route_sets_service_error(
    lb_client, list_all_resources_patch
):
    error_message = "Internal Server Error"
    module = get_module(
        dict(
            {
                "path_route_set_name": "path_route_set1",
                "load_balancer_id": "ocid1.lodbalancer.xcds",
            }
        )
    )
    list_all_resources_patch.side_effect = ServiceError(
        500, "InternalServerError", dict(), error_message
    )
    try:
        oci_load_balancer_path_route_set_facts.list_load_balancer_path_route_sets(
            lb_client, module
        )
    except Exception as ex:
        assert error_message in ex.args[0]


def create_default_path_route_set():
    path_routes = [
        {
            "path_route_set_name": "test_back_end",
            "path": "/test_resource/catalog",
            "path_match_type": PathMatchType(
                match_type=PathMatchType.MATCH_TYPE_EXACT_MATCH
            ),
        }
    ]
    path_route_set = get_path_route_set("path_route_set1", path_routes)
    return path_route_set


def get_path_route_set(name, path_routes):
    path_route_set = PathRouteSet()
    path_route_set.name = name
    path_route_set.path_routes = create_path_routes(path_routes)
    return path_route_set


def create_path_routes(path_routes):
    result_path_routes = []
    for path_routes_dict in path_routes:
        path_route = PathRoute()
        for attribute in path_route.attribute_map.keys():
            path_route.__setattr__(attribute, path_routes_dict.get(attribute))
        result_path_routes.append(path_route)
    return result_path_routes


def get_response(status, header, data, request):
    return oci.Response(status, header, data, request)


def get_module(additional_properties):
    params = dict()
    if additional_properties:
        params.update(additional_properties)
    module = FakeModule(**params)
    return module
