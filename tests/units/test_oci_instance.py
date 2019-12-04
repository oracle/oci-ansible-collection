# Copyright (c) 2017, 2018, 2019, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
import logging

from nose.plugins.skip import SkipTest

from ansible.modules.cloud.oracle import oci_instance
from ansible.module_utils.oracle.oci_utils import to_dict

try:
    import oci
    from oci.object_storage.models import Bucket
    from ansible.module_utils.oracle import oci_utils
    from oci.exceptions import ServiceError
    from oci.core.models import InstanceSourceViaBootVolumeDetails
    from oci.core.models import InstanceSourceViaImageDetails
except ImportError:
    raise SkipTest("test_oci_bucket.py requires `oci` module")


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


def setup_module():
    logging.basicConfig(
        filename="/tmp/oci_ansible_module.log", filemode="a", level=logging.INFO
    )
    oci_instance.set_logger(logging)


@pytest.fixture()
def compute_client(mocker):
    mock_cc = mocker.patch("oci.core.compute_client.ComputeClient")
    return mock_cc.return_value


@pytest.fixture()
def create_instance_source_via_image_patch(mocker):
    return mocker.patch.object(oci_instance, "_create_instance_source_via_image")


@pytest.fixture()
def get_source_details_from_module_patch(mocker):
    return mocker.patch.object(oci_instance, "get_source_details_from_module")


def get_response(status, header, data, request):
    return oci.Response(status, header, data, request)


def get_module(
    source_type="image",
    custom_boot_volume_size_in_gbs=None,
    set_top_level_image_id=False,
):
    image_id = "ocid1.image.oc1.phx....sa7klnoa"
    boot_volume_id = "ocid1.bootvolume.oc1.phx.xxxxxxExamplexxxxxxxxx"
    if source_type == "image":
        if custom_boot_volume_size_in_gbs:
            source_details = {
                "source_type": "image",
                "image_id": image_id,
                "boot_volume_size_in_gbs": custom_boot_volume_size_in_gbs,
            }
        else:
            source_details = {"source_type": "image", "image_id": image_id}
    elif source_type == "bootVolume":
        source_details = {"source_type": "bootVolume", "boot_volume_id": boot_volume_id}
    else:
        source_details = {"source_type": source_type}
    params = {
        "name": "myinstance1",
        "availability_domain": "BnQb:PHX-AD-1",
        "compartment_id": "ocid1.compartment.oc1.....vm62xq",
        "fault_domain": "FAULT-DOMAIN-1",
        "shape": "BM.Standard1.36",
        "metadata": {"foo": "bar"},
        "extended_metadata": {"baz": "quux"},
        "ipxe_script": "",
        "vnic": {
            "hostname_label": "myinstance1",
            "private_ip": "10.0.0.5",
            "subnet_id": "ocid1.subnet.oc1.phx....5iddusmpqpaoa",
        },
        "source_details": source_details,
        "wait": True,
        "wait_timeout": 1200,
    }
    if set_top_level_image_id:
        params["image_id"] = image_id
    module = FakeModule(**params)
    return module


@pytest.fixture()
def get_call_with_backoff(mocker):
    return mocker.patch.object(oci_utils, "call_with_backoff")


@pytest.fixture()
def get_oci_wait_until_patch(mocker):
    return mocker.patch.object(oci, "wait_until")


@pytest.fixture()
def get_oci_utils_create_and_wait_patch(mocker):
    return mocker.patch.object(oci_utils, "create_and_wait")


def test_launch_instance_success(compute_client, get_oci_utils_create_and_wait_patch):
    module = get_module()

    inst_created = oci.core.models.Instance()
    inst_created.display_name = module.params["name"]
    inst_created.id = "XYZ"
    inst_created.lifecycle_state = "RUNNING"
    get_oci_utils_create_and_wait_patch.return_value = {
        "changed": True,
        "instance": to_dict(inst_created),
    }

    resp = oci_instance.launch_instance(compute_client, module)
    assert resp["instance"]["lifecycle_state"] == "RUNNING"


def _get_running(inst):
    inst.id = 42
    inst.lifecycle_state = "RUNNING"
    running_resp = get_response(200, None, inst, None)
    return running_resp


def _get_stopped(inst):
    stopped = oci.core.models.Instance()
    stopped.id = inst.id
    stopped.lifecycle_state = "STOPPED"
    stopped_resp = get_response(200, None, stopped, None)
    return stopped_resp


def test_stop_running_instance_clean_first_response(
    compute_client, get_call_with_backoff, get_oci_wait_until_patch
):
    inst = oci.core.models.Instance()
    running_resp = _get_running(inst)
    stopped_resp = _get_stopped(inst)

    # The last call to get_instance must return 'stopped'
    get_call_with_backoff.side_effect = [
        running_resp,
        running_resp,
        stopped_resp,
        stopped_resp,
    ]
    compute_client.get_instance.side_effect = [running_resp, running_resp, stopped_resp]
    get_oci_wait_until_patch.return_value = None

    # The 'state' option would be set to "stopped"
    res = oci_instance.power_action_on_instance(
        compute_client, inst.id, "stopped", get_module()
    )

    # the action to take to reach the desired state must be STOP
    # compute_client.instance_action.assert_called_once_with(inst.id, "STOP")
    assert res["changed"]  # there must be a change in state

    ret_inst = res["instance"]
    # the desired state must be reached
    assert ret_inst["lifecycle_state"] == "STOPPED"


def test_create_instance_source_via_image_when_boot_volume_size_in_gbs_is_not_passed():
    module = get_module()
    instance_source_details = oci_instance._create_instance_source_via_image(
        module.params["source_details"]["image_id"]
    )
    assert (
        instance_source_details.image_id == module.params["source_details"]["image_id"]
    )
    assert instance_source_details.boot_volume_size_in_gbs is None


def test_create_instance_source_via_image_when_boot_volume_size_in_gbs_is_passed():
    module = get_module()
    boot_volume_size_in_gbs = 100
    instance_source_details = oci_instance._create_instance_source_via_image(
        module.params["source_details"]["image_id"],
        boot_volume_size_in_gbs=boot_volume_size_in_gbs,
    )
    assert (
        instance_source_details.image_id == module.params["source_details"]["image_id"]
    )
    assert instance_source_details.boot_volume_size_in_gbs == boot_volume_size_in_gbs


def test_get_source_details_from_module_ignores_image_id_top_level_module_parameter_when_source_details_exists(
    create_instance_source_via_image_patch
):
    module = get_module(set_top_level_image_id=True)
    create_instance_source_via_image_patch.return_value = InstanceSourceViaImageDetails(
        image_id=module.params["image_id"]
    )
    source_details = oci_instance.get_source_details_from_module(module)
    assert source_details.image_id == module.params["image_id"]
    create_instance_source_via_image_patch.assert_called_once_with(
        module.params["image_id"], boot_volume_size_in_gbs=None
    )


def test_get_source_details_from_module_use_image_id_top_level_module_parameter_when_source_details_does_not_exist(
    create_instance_source_via_image_patch
):
    module = get_module(set_top_level_image_id=True)
    del module.params["source_details"]
    create_instance_source_via_image_patch.return_value = InstanceSourceViaImageDetails(
        image_id=module.params["image_id"]
    )
    source_details = oci_instance.get_source_details_from_module(module)
    assert source_details.image_id == module.params["image_id"]
    create_instance_source_via_image_patch.assert_called_once_with(
        module.params["image_id"]
    )


def test_get_source_details_from_module_when_image_id_is_passed_as_source_details(
    create_instance_source_via_image_patch
):
    module = get_module()
    create_instance_source_via_image_patch.return_value = InstanceSourceViaImageDetails(
        image_id=module.params["source_details"]["image_id"]
    )
    source_details = oci_instance.get_source_details_from_module(module)
    assert source_details.image_id == module.params["source_details"]["image_id"]
    create_instance_source_via_image_patch.assert_called_once_with(
        module.params["source_details"]["image_id"], boot_volume_size_in_gbs=None
    )


def test_get_source_details_from_module_when_image_id_is_passed_as_source_details_with_boot_volume_size(
    create_instance_source_via_image_patch
):
    custom_boot_volume_size_in_gbs = 100
    module = get_module(custom_boot_volume_size_in_gbs=custom_boot_volume_size_in_gbs)
    create_instance_source_via_image_patch.return_value = InstanceSourceViaImageDetails(
        image_id=module.params["source_details"]["image_id"],
        boot_volume_size_in_gbs=module.params["source_details"][
            "boot_volume_size_in_gbs"
        ],
    )
    source_details = oci_instance.get_source_details_from_module(module)
    assert source_details.image_id == module.params["source_details"]["image_id"]
    assert (
        source_details.boot_volume_size_in_gbs
        == module.params["source_details"]["boot_volume_size_in_gbs"]
    )
    create_instance_source_via_image_patch.assert_called_once_with(
        module.params["source_details"]["image_id"], boot_volume_size_in_gbs=100
    )


def test_get_source_details_from_module_fails_for_unknown_source_type(
    create_instance_source_via_image_patch
):
    module = get_module(source_type="unknownSourceType")
    create_instance_source_via_image_patch.return_value = None
    with pytest.raises(Exception):
        oci_instance.get_source_details_from_module(module)
    assert create_instance_source_via_image_patch.call_count == 0


def test_get_launch_instance_details_calls_get_source_details_from_module(
    get_source_details_from_module_patch
):
    custom_boot_volume_size_in_gbs = 100
    module = get_module(custom_boot_volume_size_in_gbs=custom_boot_volume_size_in_gbs)
    get_source_details_from_module_patch.return_value = InstanceSourceViaImageDetails(
        image_id=module.params["source_details"]["image_id"],
        boot_volume_size_in_gbs=module.params["source_details"][
            "boot_volume_size_in_gbs"
        ],
    )
    launch_instance_details = oci_instance.get_launch_instance_details(module)
    assert (
        launch_instance_details.source_details.image_id
        == module.params["source_details"]["image_id"]
    )
    assert (
        launch_instance_details.source_details.boot_volume_size_in_gbs
        == module.params["source_details"]["boot_volume_size_in_gbs"]
    )
    get_source_details_from_module_patch.assert_called_once_with(module)
