#!/usr/bin/env python
# Copyright (c) 2018, 2019 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

"""
Oracle Cloud Infrastructure(OCI) Ansible Modules Installer Script
==============================================================
This installer script installs OCI Ansible cloud modules, its documentation fragments and utility classes in the
standard Ansible module library paths. You must have write permissions to the default Ansible installation module
library directory to run this script.

To install OCI Ansible modules, execute:
$ ./install.py
To execute the script with debug messages, execute:
$ ./install.py --debug

author: "Rohit Chaware (@rohitChaware)"
"""

from __future__ import print_function
import argparse
import os.path
import shutil
import sys
from distutils.dir_util import copy_tree

try:
    import ansible

    ANSIBLE_IS_INSTALLED = True
except ImportError:
    ANSIBLE_IS_INSTALLED = False

import pkg_resources

debug = False

MIN_OCI_PYTHON_SDK_REQUIRED = "2.2.21"


def parse_cli_args():
    parser = argparse.ArgumentParser(
        description="Script to install oci-ansible-modules"
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        default=False,
        help="Send debug messages to STDERR",
    )
    return parser.parse_args()


def log(*args, **kwargs):
    if debug:
        print(*args, file=sys.stderr, **kwargs)


def main():
    if not ANSIBLE_IS_INSTALLED:
        print(
            "Could not load ansible module. To install ansible, use <pip install ansible>."
        )
        sys.exit(1)

    installed_packages = dict(
        [(pkg.project_name, pkg.version) for pkg in pkg_resources.working_set]
    )

    if "oci" not in installed_packages:
        print(
            "OCI Python SDK version-{0} is required for using oci-ansible-modules. To install OCI Python SDK, use"
            " < pip install oci=={0} >.".format(MIN_OCI_PYTHON_SDK_REQUIRED)
        )

    elif installed_packages["oci"] < MIN_OCI_PYTHON_SDK_REQUIRED:
        print(
            "Please install version >= {0} of OCI Python SDK. Use < pip install oci=={0} >.".format(
                MIN_OCI_PYTHON_SDK_REQUIRED
            )
        )

    global debug
    args = parse_cli_args()
    if args.debug:
        debug = True

    ansible_path = os.path.dirname(os.path.abspath(os.path.realpath(ansible.__file__)))
    log("Ansible path: {}".format(ansible_path))

    module_utils_path = os.path.join(ansible_path, "module_utils")
    if not os.path.exists(module_utils_path):
        print("Module utilities directory {} does not exist.".format(module_utils_path))
        sys.exit(1)
    if not os.path.isdir(module_utils_path):
        print("Module utilities path {} is not a directory.".format(module_utils_path))
        sys.exit(1)
    log("Module utilities path: {}".format(module_utils_path))


    ### document fragments copy ###
    document_fragments_path_old = os.path.join(
        ansible_path, "utils", "module_docs_fragments"
    )
    document_fragments_path_new = os.path.join(ansible_path, "plugins", "doc_fragments")
    if os.path.exists(document_fragments_path_new):
        document_fragments_path = document_fragments_path_new
    elif os.path.exists(document_fragments_path_old):
        document_fragments_path = document_fragments_path_old
    else:
        print(
            "Documentation fragments directory {0} or {1} does not exist".format(
                document_fragments_path_old, document_fragments_path_new
            )
        )
        sys.exit(1)
    if not os.path.isdir(document_fragments_path):
        print(
            "Documentation fragments path {} is not a directory".format(
                document_fragments_path
            )
        )
        sys.exit(1)
    log("Documentation fragments path: {}".format(document_fragments_path))
    current_path = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))
    doc_src_path = os.path.join(current_path, "module_docs_fragments")
    print(
        "Copying documentation fragments from {} to {}".format(
            doc_src_path, document_fragments_path
        )
    )
    copy_files(os.listdir(doc_src_path), doc_src_path, document_fragments_path)

    ### Utils copy ###
    utilities_src_path = os.path.join(current_path, "module_utils", "oracle")
    utilities_dest_path = os.path.join(module_utils_path, "oracle")
    if not os.path.exists(utilities_dest_path):
        os.mkdir(utilities_dest_path)
    print(
        "Copying oracle utility files from {} to {}".format(
            utilities_src_path, utilities_dest_path
        )
    )
    copy_tree(utilities_src_path, utilities_dest_path)

    ### Inventory plugin copy ###
    inventory_plugin_src_path = os.path.join(current_path, "inventory_plugins")
    inventory_plugin_dest_path = os.path.join(ansible_path, "plugins", "inventory")
    if not os.path.exists(inventory_plugin_dest_path):
        os.mkdir(inventory_plugin_dest_path)
    print(
        "Copying oracle inventory plugin files from {} to {}".format(
            inventory_plugin_src_path, inventory_plugin_dest_path
        )
    )
    copy_files(
        os.listdir(inventory_plugin_src_path), inventory_plugin_src_path, inventory_plugin_dest_path
    )

    ### Modules copy ###
    oracle_module_dir_path = os.path.join(ansible_path, "modules", "cloud", "oracle")
    if not os.path.exists(oracle_module_dir_path):
        print("Creating directory {}".format(oracle_module_dir_path))
        os.mkdir(oracle_module_dir_path)

    # Modules in oci-ansible-modules are stored in library directory.
    roles_library_path = os.path.join(current_path, "library")
    log("Roles library path: {}".format(roles_library_path))

    print(
        "Copying OCI Ansible modules from {} to {}".format(
            roles_library_path, oracle_module_dir_path
        )
    )
    copy_files(
        os.listdir(roles_library_path), roles_library_path, oracle_module_dir_path
    )

    print("OCI Ansible modules installed successfully.")


def copy_files(files, src_dir, dest_dir):
    if type(files) is not list:
        files = [files]
    for file in files:
        src_file_path = os.path.join(src_dir, file)
        dest_file_path = os.path.join(dest_dir, file)
        if os.path.exists(src_file_path):
            if os.path.exists(dest_file_path):
                print("Overwriting {}".format(dest_file_path))
            else:
                log("Copying to {}".format(dest_file_path))
            shutil.copy(src_file_path, dest_file_path)


if __name__ == "__main__":
    main()
