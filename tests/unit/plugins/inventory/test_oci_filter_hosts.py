# Copyright (c) 2026 Oracle and/or its affiliates.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Unit tests for InventoryModule._filter_hosts template evaluation."""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import importlib.util
import os
import sys
import types
from unittest.mock import MagicMock

import pytest
from ansible.parsing.dataloader import DataLoader
from ansible.template import Templar

REPO_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "..", "..")
)
INVENTORY_PLUGIN_PATH = os.path.join(REPO_ROOT, "plugins", "inventory", "oci.py")


def _stub_optional_imports():
    """Inventory plugin imports OCI SDK and collection helpers; stub them for unit tests."""
    names = [
        "ansible_collections",
        "ansible_collections.oracle",
        "ansible_collections.oracle.oci",
        "ansible_collections.oracle.oci.plugins",
        "ansible_collections.oracle.oci.plugins.module_utils",
    ]
    for name in names:
        if name not in sys.modules:
            sys.modules[name] = types.ModuleType(name)

    module_utils = sys.modules[
        "ansible_collections.oracle.oci.plugins.module_utils"
    ]
    module_utils.oci_common_utils = MagicMock()
    module_utils.oci_version = MagicMock()
    module_utils.oci_version_utils = MagicMock()
    module_utils.oci_config_utils = MagicMock()

    oci_modules = [
        "oci",
        "oci.core",
        "oci.core.compute_client",
        "oci.identity",
        "oci.identity.identity_client",
        "oci.core.virtual_network_client",
        "oci.database",
        "oci.util",
        "oci.exceptions",
        "oci.auth",
        "oci.auth.signers",
        "oci.auth.signers.resource_principals_signer",
    ]
    for name in oci_modules:
        if name not in sys.modules:
            sys.modules[name] = MagicMock()


def _load_inventory_module():
    _stub_optional_imports()
    module_name = "oci_inventory_filter_hosts_under_test"
    # Drop a previously loaded copy so ImportError fallback tests can reload.
    sys.modules.pop(module_name, None)
    spec = importlib.util.spec_from_file_location(module_name, INVENTORY_PLUGIN_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    sys.modules[module_name] = module
    return module


def _make_plugin(inventory_module, templar=None):
    plugin = inventory_module.InventoryModule.__new__(inventory_module.InventoryModule)
    plugin.templar = templar if templar is not None else Templar(loader=DataLoader())
    plugin.debug = lambda *args, **kwargs: None
    plugin.get_option = lambda option: False
    return plugin


@pytest.fixture
def inventory_module():
    return _load_inventory_module()


def test_filter_hosts_evaluates_jinja_condition_on_ansible_core_2_19(inventory_module):
    """False conditions must not match. On ansible-core 2.19+ this requires trust_as_template."""
    plugin = _make_plugin(inventory_module)
    hostvars = {"lifecycle_state": "RUNNING", "id": "ocid1.instance.example"}

    assert (
        plugin._filter_hosts(["lifecycle_state == 'STOPPED'"], hostvars) is False
    )
    assert (
        plugin._filter_hosts(["lifecycle_state == 'RUNNING'"], hostvars) is True
    )


def test_filter_hosts_fallback_when_trust_as_template_unavailable(monkeypatch, inventory_module):
    """ansible-core < 2.19 has no trust_as_template; wrapping must still reach templar.template."""
    import ansible.template as ansible_template

    original_import = __import__

    def import_without_trust_as_template(name, globals=None, locals=None, fromlist=(), level=0):
        module = original_import(name, globals, locals, fromlist, level)
        if name == "ansible.template" or (fromlist and name == "ansible"):
            if fromlist and "trust_as_template" in fromlist:
                raise ImportError("simulated ansible-core < 2.19")
        return module

    monkeypatch.setattr("builtins.__import__", import_without_trust_as_template)
    if hasattr(ansible_template, "trust_as_template"):
        monkeypatch.delattr(ansible_template, "trust_as_template", raising=False)

    reloaded = _load_inventory_module()
    templar = MagicMock()
    templar.template.return_value = False
    plugin = _make_plugin(reloaded, templar=templar)

    result = plugin._filter_hosts(
        ["lifecycle_state == 'RUNNING'"], {"lifecycle_state": "RUNNING"}
    )

    assert result is False
    templar.template.assert_called_once()
    rendered = templar.template.call_args[0][0]
    assert rendered == "{{lifecycle_state == 'RUNNING'}}"
