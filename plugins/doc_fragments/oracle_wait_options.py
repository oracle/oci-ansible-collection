# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type


class ModuleDocFragment(object):
    DOCUMENTATION = """
    options:
        wait:
            description: Whether to wait for create or delete operation to complete.
            default: yes
            type: bool
        wait_timeout:
            description: Time, in seconds, to wait when I(wait=yes). Defaults to 1200 for most of the services but some
                         services might have a longer wait timeout.
            type: int
    """
