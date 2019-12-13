#!/usr/bin/env python
# coding: utf-8
# Copyright (c) 2019, Oracle and/or its affiliates. All rights reserved.
#
# Usage: python format_generated_descriptions.py "~/dev/SDK/ansible-cloud-module/ansible/lib/ansible/modules/cloud/oracle/oci_*.py"
#
import os
import glob
import sys

import textwrap

if len(sys.argv) < 2:
    sys.exit("Usage Error: Must pass 1 argument containing pattern of files to format")

ALL_MODULES_PATTERN = os.path.expanduser(sys.argv[1])
GENERATED_FILE_HEADER = "GENERATED FILE - DO NOT EDIT"

def get_all_files():
    all_module_files = glob.glob(ALL_MODULES_PATTERN)
    if len(all_module_files) == 0:
        print("No modules found matching pattern: {}".format(ALL_MODULES_PATTERN))
        sys.exit(0)

    return all_module_files


def delete_if_generated(file_path):
    with open(file_path, "r") as f:
        content = f.read()
    
    if GENERATED_FILE_HEADER in content:
        print('Deleting file: {}'.format(file_path))
        os.remove(file_path)


def main():
    all_module_files = get_all_files()
    for path in all_module_files:
        delete_if_generated(path)


if __name__ == "__main__":
    main()
