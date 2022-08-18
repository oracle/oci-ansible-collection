# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import logging
import time

VERBOSITY_TO_LOG_LEVEL_MAPPING = {
    0: logging.NOTSET,
    1: logging.WARNING,
    2: logging.INFO,
    3: logging.DEBUG,
}


class LogContainer:
    def __init__(self):
        self._container = []

    def append(self, msg):
        self._container.append(msg)

    def get_logs(self):
        return self._container


LOG_CONTAINER = LogContainer()


class InMemoryHandler(logging.Handler):
    def __init__(self, container, level):
        self._container = container
        super(InMemoryHandler, self).__init__(level)

    def emit(self, record):
        msg = self.format(record)
        self._container.append(msg)


def get_in_memory_handler(container, formatter, level):
    handler = InMemoryHandler(container, level)
    handler.setFormatter(formatter)
    return handler


class LogFormatter(logging.Formatter):
    def __init__(self, converter, fmt=None, datefmt=None):
        self.converter = converter
        super(LogFormatter, self).__init__(fmt=fmt, datefmt=datefmt)


def setup_logging(verbosity=0):
    if verbosity >= 3:
        log_level = logging.DEBUG
    else:
        log_level = VERBOSITY_TO_LOG_LEVEL_MAPPING.get(verbosity)

    in_memory_handler = get_in_memory_handler(
        LOG_CONTAINER,
        LogFormatter(
            converter=time.gmtime,
            fmt="%(asctime)s %(levelname)3s %(filename)s:%(lineno)s %(message)s",
            datefmt="%Y-%m-%d,%H:%M:%S %Z",
        ),
        log_level,
    )
    logging.basicConfig(level=log_level, handlers=[in_memory_handler])
