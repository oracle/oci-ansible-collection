# Copyright (c) 2019, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.


class ModuleDocFragment(object):
    DOCUMENTATION = """
    options:
        sort_order:
            description: The order in which to sort the results.
            required: false
            type: str
            choices: ['ASC', 'DESC']
    """
