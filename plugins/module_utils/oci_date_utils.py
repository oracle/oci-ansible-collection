# Copyright (c) 2019 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from ansible.module_utils import six
from datetime import datetime


def parse_iso8601_str_as_datetime(date_string):
    """
    Converts string to datetime.

    The string should be in iso8601 datetime format. Returns the original value if it is not in expected format.

    :param string: str.
    :return: datetime.
    """
    if not date_string:
        return date_string
    if not isinstance(date_string, six.string_types):
        return date_string
    date_string_utc = date_string.replace("+00:00", "Z")
    try:
        naivedatetime = datetime.strptime(date_string_utc, "%Y-%m-%dT%H:%M:%S.%fZ")
    except ValueError:
        pass
    else:
        return naivedatetime

    try:
        # try without microsecond
        naivedatetime = datetime.strptime(date_string_utc, "%Y-%m-%dT%H:%M:%SZ")
    except ValueError:
        return date_string
    else:
        return naivedatetime
