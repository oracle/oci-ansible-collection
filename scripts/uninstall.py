#!/usr/bin/env python
# Copyright (c) 2018, 2019 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

"""
Oracle Cloud Infrastructure(OCI) Ansible Modules Uninstaller Script
===================================================================
This script deletes OCI Ansible modules, Oracle docs fragments and Oracle Ansible utility file from the ansible path.

To uninstall OCI Ansible modules, execute:
$ ./uninstall.py
To execute the script with debug messages, execute:
$ ./uninstall.py --debug

author: "Rohit Chaware (@rohitChaware)"
"""

from __future__ import print_function
import argparse
import os.path
import shutil
import sys

try:
    import ansible

    ANSIBLE_IS_INSTALLED = True
except ImportError:
    ANSIBLE_IS_INSTALLED = False

debug = False


def parse_cli_args():
    parser = argparse.ArgumentParser(description="Script to uninstall oci-ansible-role")
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
        print("Could not load ansible module.")
        sys.exit(1)
    global debug
    args = parse_cli_args()
    if args.debug:
        debug = True

    ansible_path = os.path.dirname(os.path.abspath(os.path.realpath(ansible.__file__)))
    log("Ansible path: {}".format(ansible_path))

    module_utils_path = os.path.join(ansible_path, "module_utils", "oracle")
    log("Module utilities path: {}".format(module_utils_path))

    document_fragments_path_old = os.path.join(
        ansible_path, "utils", "module_docs_fragments"
    )
    document_fragments_path_new = os.path.join(ansible_path, "plugins", "doc_fragments")
    if os.path.exists(document_fragments_path_new):
        document_fragments_path = document_fragments_path_new
    else:
        document_fragments_path = document_fragments_path_old

    log("Documentation fragments path: {}".format(document_fragments_path))

    delete(module_utils_path)

    oci_docs_fragments = []
    for filename in os.listdir(document_fragments_path):
        if filename.startswith("oracle"):
            oci_docs_fragments.append(os.path.join(document_fragments_path, filename))

    delete(oci_docs_fragments)

    oracle_module_dir_path = os.path.join(ansible_path, "modules", "cloud", "oracle")
    delete(oracle_module_dir_path)

    print("Uninstalled OCI Ansible modules successfully.")


def delete(paths):
    if type(paths) is not list:
        paths = [paths]

    for path in paths:
        if os.path.isdir(path):
            print("Deleting directory {}".format(path))
            shutil.rmtree(path)
        elif os.path.isfile(path):
            print("Deleting {}".format(path))
            os.remove(path)


if __name__ == "__main__":
    main()
