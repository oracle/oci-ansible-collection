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
from ansible.module_utils.six.moves import http_client  # noqa

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


def _httpclient_debug_logging_patch():
    """Enable HTTPConnection debug logging to the logging framework"""
    try:
        httpclient_logger = logging.getLogger("http.client")

        def httpclient_log(*args):
            # adding logs at debug level
            httpclient_logger.debug(" ".join(args))

        # mask the print() built-in in the http.client module to use
        # logging instead
        # patching the print method is not valid Python 2 syntax so
        # we have to use exec to avoid a SyntaxError when running with
        # python 2
        # (Note: you can only try / except a SyntaxError if it is inside
        # an exec or eval block)
        exec("http_client.print = httpclient_log") in {}
    except Exception:
        # this is best effort to output additional logging, we never want to
        # fail the module if anything in here fails
        pass


def get_log_level(verbosity=0):
    """ fetches log_level based on environment-variable or verbosity """

    env_log_level = os.getenv("OCI_ANSIBLE_LOG_LEVEL")
    # logging using environment variable has the higher priority
    if env_log_level is not None:
        # assumption: default log_level incase environment variable doesn't map to any level will be NONE &
        # won't check verbosity levels respecting user who opted for environment variable
        return ENV_VAR_TO_LOG_LEVEL_MAPPING.get(env_log_level)

    # As of now we are keeping LOG_LEVEL for backward compatibility. We will remove it later on
    old_env_log_level = os.getenv("LOG_LEVEL")
    if old_env_log_level is not None:
        return ENV_VAR_TO_LOG_LEVEL_MAPPING.get(old_env_log_level)

    # logging using verbosity
    if verbosity >= 3:
        return logging.DEBUG
    return VERBOSITY_TO_LOG_LEVEL_MAPPING.get(verbosity)


def get_log_dir():
    """ fetches log_dir based on environment variables """
    env_log_dir = os.getenv("OCI_ANSIBLE_LOG_DIR")
    if env_log_dir is not None:
        return os.path.expanduser(os.path.expandvars(env_log_dir))

    # As of now we are keeping LOG_PATH for backward compatibility. We will remove it later on
    old_env_log_path = os.getenv("LOG_PATH")
    if old_env_log_path is not None:
        return os.path.expanduser(os.path.expandvars(old_env_log_path))
    return None


def setup_logging(log_level, log_dir):

    if log_level is None:
        # Disable the logging in this case
        logging.basicConfig(handlers=[logging.NullHandler()])
        return
    if log_level == logging.DEBUG:
        # adding http connection debug logs
        _httpclient_debug_logging_patch()

    oci_ansible_log_format = (
        "%(asctime)s %(levelname)3s %(filename)s:%(lineno)s %(message)s"
    )
    oci_ansible_log_date_format = "%Y-%m-%d,%H:%M:%S"

    if log_dir is None:
        # log to console
        in_memory_handler = get_handler(
            "InMemoryHandler",
            LOG_CONTAINER,
            LogFormatter(
                converter=time.gmtime,
                fmt=oci_ansible_log_format,
                datefmt=oci_ansible_log_date_format,
            ),
            log_level,
        )
        logging.basicConfig(level=log_level, handlers=[in_memory_handler])
        return

    # assuming: log_dir will be a folder & not a file
    log_file_path = os.path.join(log_dir, "oci_ansible_module.log")
    # check write access if the file exists
    if os.path.exists(log_dir) and (
        not os.path.exists(log_file_path) or os.access(log_file_path, os.W_OK)
    ):
        # log into a file
        file_handler = get_handler(
            "FileHandler",
            log_file_path,
            LogFormatter(
                converter=time.gmtime,
                fmt=oci_ansible_log_format,
                datefmt=oci_ansible_log_date_format,
            ),
            log_level,
        )
        logging.basicConfig(level=log_level, handlers=[file_handler])
        return

    # Disable the logging by default
    logging.basicConfig(handlers=[logging.NullHandler()])
