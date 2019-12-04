#!/usr/bin/env python2

# Copyright (c) 2017, 2018, 2019, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

# Run the integration tests under ansible/test/integration/targets
# without using "ansible-test".
# This file uses the logic in ansible/test/runner/lib/executor.py
# Execute this as $ run-integration-test-target-in-venv.py <name-of-integration-test-target>.
# For example: $ run-integration-test-target-in-venv.py oci_object_storage

import tempfile
import sys
import os
from subprocess import call

target = sys.argv[1]

# Create a playbook yaml representation of the target we want to run
playbook = '''
- hosts: %s
  gather_facts: %s
  roles:
    - { role: %s }
    ''' % ("localhost", True, target)

print(playbook)

# Create a temporary file having the playbook contents
with tempfile.NamedTemporaryFile(dir="/tmp", prefix='%s-' % target, suffix=".yml") as tempyaml:
    tempyaml.write(playbook.encode('utf-8'))
    tempyaml.flush()
    extra_vars_file = os.environ.get("EXTRA_VARS_FILE")
    if extra_vars_file and os.path.isfile(extra_vars_file):
        cmd = ['ansible-playbook', tempyaml.name, "--extra-vars", "@" + extra_vars_file]
    else:
        cmd = ['ansible-playbook', tempyaml.name]

    # run playbook
    print(cmd)
    return_code = call(cmd)
    sys.exit(return_code)

