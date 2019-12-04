# Copyright (c) 2018, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
import logging
from ansible.modules.cloud.oracle import oci_load_balancer_path_route_set
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
    raise SkipTest("test_oci_load_balancer_path_route_set.py requires `oci` module")


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
def create_path_route_set_patch(mocker):
    return mocker.patch.object(
        oci_load_balancer_path_route_set, "create_path_route_set"
    )


@pytest.fixture()
def update_path_route_set_patch(mocker):
    return mocker.patch.object(
        oci_load_balancer_path_route_set, "update_path_route_set"
    )


@pytest.fixture()
def create_or_update_lb_resources_and_wait_patch(mocker):
    return mocker.patch.object(oci_lb_utils, "create_or_update_lb_resources_and_wait")


@pytest.fixture()
def delete_lb_resources_and_wait_patch(mocker):
    return mocker.patch.object(oci_lb_utils, "delete_lb_resources_and_wait")


@pytest.fixture()
def check_and_create_resource_patch(mocker):
    return mocker.patch.object(oci_utils, "check_and_create_resource")


@pytest.fixture()
def get_existing_resource_patch(mocker):
    return mocker.patch.object(oci_utils, "get_existing_resource")


def setUpModule():
    logging.basicConfig(
        filename="/tmp/oci_ansible_module.log", filemode="a", level=logging.INFO
    )
    oci_load_balancer_path_route_set.set_logger(logging)


def test_create_or_update_path_route_set_create(
    lb_client, check_and_create_resource_patch, get_existing_resource_patch
):
    module = get_module(dict())
    path_route_set = create_default_path_route_set()
    get_existing_resource_patch.return_value = None
    check_and_create_resource_patch.return_value = {
        "path_route_set": to_dict(path_route_set),
        "changed": True,
    }
    result = oci_load_balancer_path_route_set.create_or_update_path_route_set(
        lb_client, module
    )
    assert result["path_route_set"]["name"] is path_route_set.name


def test_create_or_update_path_route_set_update(
    lb_client, update_path_route_set_patch, get_existing_resource_patch
):
    module = get_module(dict())
    path_route_set = create_default_path_route_set()
    get_existing_resource_patch.return_value = path_route_set
    update_path_route_set_patch.return_value = {
        "path_route_set": to_dict(path_route_set),
        "changed": True,
    }
    result = oci_load_balancer_path_route_set.create_or_update_path_route_set(
        lb_client, module
    )
    assert result["path_route_set"]["name"] is path_route_set.name


def test_create_or_update_path_route_set_service_error(
    lb_client, check_and_create_resource_patch, get_existing_resource_patch
):
    module = get_module(dict())
    error_message = "Internal Server Error"
    check_and_create_resource_patch.side_effect = ServiceError(
        500, "InternalServerError", dict(), error_message
    )
    get_existing_resource_patch.return_value = None
    try:
        oci_load_balancer_path_route_set.create_or_update_path_route_set(
            lb_client, module
        )
    except Exception as ex:
        assert error_message in ex.args[0]


def test_create_or_update_path_route_set_client_error(
    lb_client, check_and_create_resource_patch, get_existing_resource_patch
):
    module = get_module(dict())
    error_message = "Work Request Failed"
    check_and_create_resource_patch.side_effect = ClientError(
        Exception("Work Request Failed")
    )
    get_existing_resource_patch.return_value = None
    try:
        oci_load_balancer_path_route_set.create_or_update_path_route_set(
            lb_client, module
        )
    except Exception as ex:
        assert error_message in ex.args[0]


def test_create_path_route_set(lb_client, create_or_update_lb_resources_and_wait_patch):
    module = get_module(
        dict(
            path_routes=[
                {
                    "backend_set_name": "test_back_end",
                    "path": "/test_resource/catalog",
                    "path_match_type": dict(
                        match_type=PathMatchType.MATCH_TYPE_EXACT_MATCH
                    ),
                }
            ]
        )
    )
    path_route_set = create_default_path_route_set()
    create_or_update_lb_resources_and_wait_patch.return_value = {
        "path_route_set": to_dict(path_route_set),
        "changed": True,
    }
    result = oci_load_balancer_path_route_set.create_path_route_set(lb_client, module)
    assert result["path_route_set"]["name"] == path_route_set.name


def test_update_path_route_set_purge_old_path_routes(
    lb_client, create_or_update_lb_resources_and_wait_patch
):
    module = get_module(
        dict(
            path_routes=[
                {
                    "backend_set_name": "test_back_end",
                    "path": "/test_resource/catalog",
                    "path_match_type": dict(
                        match_type=PathMatchType.MATCH_TYPE_PREFIX_MATCH
                    ),
                }
            ],
            name="path_route_set1",
            purge_path_routes=True,
        )
    )
    path_route_set = create_default_path_route_set()
    create_or_update_lb_resources_and_wait_patch.return_value = {
        "path_route_set": to_dict(path_route_set),
        "changed": True,
    }
    result = oci_load_balancer_path_route_set.update_path_route_set(
        lb_client, module, "ocid1.loadbalancer.aaa", path_route_set, "path_route_set1"
    )
    assert result["changed"] is True


def test_update_path_route_set_purge_empty_path_routes(
    lb_client, create_or_update_lb_resources_and_wait_patch
):
    module = get_module(
        dict(path_routes=[], name="path_route_set1", purge_path_routes=True)
    )
    path_route_set = create_default_path_route_set()
    create_or_update_lb_resources_and_wait_patch.return_value = {
        "path_route_set": to_dict(path_route_set),
        "changed": True,
    }
    result = oci_load_balancer_path_route_set.update_path_route_set(
        lb_client, module, "ocid1.loadbalancer.aaa", path_route_set, "path_route_set1"
    )
    assert result["changed"] is True


def test_update_path_route_set_append_new_path_routes(
    lb_client, create_or_update_lb_resources_and_wait_patch
):
    module = get_module(
        dict(
            path_routes=[
                {
                    "backend_set_name": "test_back_end",
                    "path": "/test_resource/catalog",
                    "path_match_type": dict(
                        match_type=PathMatchType.MATCH_TYPE_PREFIX_MATCH
                    ),
                }
            ],
            name="path_route_set1",
            purge_path_routes=False,
        )
    )
    path_route_set = create_default_path_route_set()
    create_or_update_lb_resources_and_wait_patch.return_value = {
        "path_route_set": to_dict(path_route_set),
        "changed": True,
    }
    result = oci_load_balancer_path_route_set.update_path_route_set(
        lb_client, module, "ocid1.loadbalancer.aaa", path_route_set, "path_route_set1"
    )
    assert result["changed"] is True


def test_delete_path_route_set(lb_client, delete_lb_resources_and_wait_patch):
    module = get_module(dict())
    path_route_set = create_default_path_route_set()
    delete_lb_resources_and_wait_patch.return_value = {
        "path_route_set": to_dict(path_route_set),
        "changed": True,
    }
    result = oci_load_balancer_path_route_set.delete_path_route_set(lb_client, module)
    assert result["changed"] is True


def create_default_path_route_set():
    path_routes = [
        {
            "backend_set_name": "test_back_end",
            "path": "/test_resource/catalog",
            "path_match_type": dict(match_type=PathMatchType.MATCH_TYPE_EXACT_MATCH),
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
