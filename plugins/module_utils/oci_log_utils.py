# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import logging
import time
import os

VERBOSITY_TO_LOG_LEVEL_MAPPING = {
    1: logging.WARNING,
    2: logging.INFO,
    3: logging.DEBUG,
}

ENV_VAR_TO_LOG_LEVEL_MAPPING = {
    "WARNING": logging.WARNING,
    "INFO": logging.INFO,
    "DEBUG": logging.DEBUG,
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


class FileHandler(logging.FileHandler):
    def __init__(self, filename, level):
        self.level = level
        super(FileHandler, self).__init__(filename=filename)


HANDLER_MAPPING = {
    "InMemoryHandler": InMemoryHandler,
    "FileHandler": FileHandler,
}


def get_handler(handler_type, container, formatter, level):
    handler = HANDLER_MAPPING.get(handler_type)(container, level)
    handler.setFormatter(formatter)
    return handler


class LogFormatter(logging.Formatter):
    def __init__(self, converter, fmt=None, datefmt=None):
        self.converter = converter
        super(LogFormatter, self).__init__(fmt=fmt, datefmt=datefmt)


def setup_logging(verbosity=0):
    """Setup logging configuration"""
    env_log_path = "OCI_ANSIBLE_LOG_PATH"
    env_log_level = "OCI_ANSIBLE_LOG_LEVEL"

    # As of now we are keeping LOG_PATH & LOG_LEVEL for backward compatibility. We will remove it later on
    old_env_log_path = "LOG_PATH"
    old_env_log_level = "LOG_LEVEL"

    log_path = os.getenv(env_log_path) or os.getenv(old_env_log_path)
    log_level_str = os.getenv(env_log_level) or os.getenv(old_env_log_level)
    if log_level_str is not None:
        # logging using environment variable has the higher priority
        # assumption: default log_level incase environment variable doesn't map to any level will be NONE &
        # won't check verbosity levels respecting user who opted for environment variable
        log_level = ENV_VAR_TO_LOG_LEVEL_MAPPING.get(log_level_str, None)
    else:
        # logging using verbosity
        if verbosity >= 3:
            log_level = logging.DEBUG
        else:
            log_level = VERBOSITY_TO_LOG_LEVEL_MAPPING.get(verbosity, None)

    if log_level is not None:
        if log_path is not None:
            # logging using environment variable has the higher priority
            log_path = os.path.expanduser(os.path.expandvars(log_path))
            # assuming: log_path will be a folder & not a file
            log_file_path = os.path.join(log_path, "oci_ansible_module.log")
            # check write access
            # assumption: incase the below condition is not true, won't log the details to console
            # respecting user who opted for environment variable
            if os.path.exists(log_path) and (
                not os.path.exists(log_file_path) or os.access(log_file_path, os.W_OK)
            ):
                file_handler = get_handler(
                    "FileHandler",
                    log_file_path,
                    LogFormatter(
                        converter=time.gmtime,
                        fmt="%(asctime)s %(levelname)3s %(filename)s:%(lineno)s %(message)s",
                        datefmt="%Y-%m-%d,%H:%M:%S %Z",
                    ),
                    log_level,
                )
                logging.basicConfig(level=log_level, handlers=[file_handler])
        else:
            # log to console
            in_memory_handler = get_handler(
                "InMemoryHandler",
                LOG_CONTAINER,
                LogFormatter(
                    converter=time.gmtime,
                    fmt="%(asctime)s %(levelname)3s %(filename)s:%(lineno)s %(message)s",
                    datefmt="%Y-%m-%d,%H:%M:%S %Z",
                ),
                log_level,
            )
            logging.basicConfig(level=log_level, handlers=[in_memory_handler])
