#!/usr/bin/env python
# coding: utf-8
# Copyright (c) 2020, Oracle and/or its affiliates. All rights reserved.

import os
import argparse
import subprocess
import sys
import math
import json


def test_targets(targets, tags, skip_tags):

    ansible_test_args = ["ansible-test", "integration"]
    if targets:
        ansible_test_args.extend(targets)

    if tags:
        ansible_test_args.extend(["--tags", tags])

    if skip_tags:
        ansible_test_args.extend(["--skip-tags", skip_tags])

    print('ansible test args: {}'.format(str(ansible_test_args)))

    cwd = os.environ.get("COLLECTION_DIR")
    if not cwd:
        cwd = os.getcwd()

    subprocess.run(ansible_test_args, cwd=cwd, check=True)

def main(targets, set_no, total_target_sets, tags, skip_tags):

    # split targets into sets
    num_targets = len(targets)
    set_size = math.ceil(num_targets / total_target_sets)

    sets = []
    for i in range(0, total_target_sets):
        start_target_index = i*set_size
        end_target_index = start_target_index + set_size
        if end_target_index > len(targets):
            end_target_index = len(targets)

        sets.append(targets[start_target_index:end_target_index])

    print("Target sets:")
    for i in range(0, len(sets)):
        print("Set {}\t: {}".format(i, str(sets[i])))

    targets_to_run = sets[set_no]
    if len(targets_to_run) == 0:
        print("Skipping empty target set")
    else:
        test_targets(targets_to_run, tags, skip_tags)


if __name__== "__main__":
    parser = argparse.ArgumentParser(description='Run integration tests for oci ansible collection.')
    parser.add_argument('--targets', required=True, help='A list of paths of all the integration tests targets')
    parser.add_argument('--set-no', type=int, help='A number representing the set number of the job calling the script')
    parser.add_argument('--total-target-sets', type=int, help='A number representing the total number of sets')
    parser.add_argument('--ansible-test-tags', help='A value for the --tags argument to ansible-test to indicate which tests to run')
    parser.add_argument('--ansible-test-skip-tags', help='A value for the --skip-tags argument to ansible-test to indicate which tests to skip')

    args = parser.parse_args()

    if args.set_no is not None and args.total_target_sets is None:
        sys.exit("ERROR: If --set-no is specified, --total-target-sets must be specified")

    if args.set_no is not None and args.set_no >= args.total_target_sets:
        sys.exit("ERROR: set_no must be <= number of sets")

    total_target_sets = args.total_target_sets
    set_no = args.set_no
    if set_no is None:
        print("No set_no specified, running all sets")
        total_target_sets = 1
        set_no = 0

    # split up targets by whitespace, that is how we get them from the grep in .gitlab-ci.yaml
    targets = args.targets.split()

    targets = [ os.path.basename(target) for target in targets ]

    print("Current working directory: {}".format(os.getcwd()))
    print("Targets: {}".format(str(targets)))
    print("Set number: {}".format(args.set_no))
    print("Total target sets: {}".format(args.total_target_sets))

    print("Environment:")
    print(json.dumps(dict(os.environ), indent=2))

    main(
        targets,
        set_no,
        total_target_sets,
        args.ansible_test_tags,
        args.ansible_test_skip_tags
    )
