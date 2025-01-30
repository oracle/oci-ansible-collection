# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.
# GENERATED FILE - DO NOT EDIT - MANUAL CHANGES WILL BE OVERWRITTEN

from __future__ import absolute_import, division, print_function

__metaclass__ = type
from jinja2.runtime import Undefined


class FilterModule(object):
    def filters(self):
        return {"override": self.override_filter}

    """
    A filter to allow optionally overriding a default value.

    Usage:
    example_module:
        a: "{{ 8 | override(example_override_cpu_count, omit) }}"

    If example_override_cpu_count is defined and has a value other than null, it will be used.
    If example_override_cpu_count is undefined, 8 will be used.
    If example_override_cpu_count is explicitly set to null, the field will be omitted.
    """

    def override_filter(self, hardcoded_default, override, omit):
        if override is None:
            # override is explicitly set to null which indicates
            # this field should be omitted
            return omit
        elif isinstance(override, Undefined):
            # override is undefined so use the default value
            return hardcoded_default
        else:
            # override has some value so use that
            return override
