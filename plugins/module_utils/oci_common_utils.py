# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function
from contextlib import contextmanager
from multiprocessing.pool import ThreadPool

__metaclass__ = type
from ansible.module_utils import six
from ansible.module_utils.six.moves import http_client
from datetime import datetime
import tempfile
import logging
import os
import re
import sys
import json

try:
    os.environ["OCI_PYTHON_SDK_NO_SERVICE_IMPORTS"] = "1"
    import oci
    from oci.retry import DEFAULT_RETRY_STRATEGY
    from oci.exceptions import ServiceError

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False

MAX_WAIT_TIMEOUT_IN_SECONDS = 1200
# some services like waas have longer wait times. This map allows to specify wait times at a service level so that
# we need not override for each module in a service.
SERVICE_WAIT_TIMEOUT_MAP = {
    "waas": 2400,
    "analytics": 2000,
    "mysql": 2400,
    "bds": 4000,
    "database": 3600,
}
DEAD_STATES = [
    "TERMINATING",
    "TERMINATED",
    "FAULTY",
    "FAILED",
    "DELETING",
    "DELETED",
    "PENDING_DELETION",
    "UNKNOWN_ENUM_VALUE",
    "DETACHING",
    "DETACHED",
]

# If a resource is in one of these states it would be considered available
DEFAULT_READY_STATES = [
    "AVAILABLE",
    "ACTIVE",
    "RUNNING",
    "PROVISIONED",
    "ATTACHED",
    "ASSIGNED",
    "ENABLED",
    "SUCCEEDED",
    "PENDING_PROVIDER",
]

CANCELLED_STATES = ["CANCELED", "CANCELLED"]
FAILED_STATES = ["FAILED"]

WORK_REQUEST_COMPLETED_STATES = ["SUCCEEDED", "SUCCESS", "FAILED", "COMPLETED"]
WORK_REQUEST_SUCCESS_STATES = ["SUCCEEDED", "SUCCESS"]
WORK_REQUEST_FAILED_STATES = FAILED_STATES

# If a resource is in one of these states, it would be considered deleted
DEFAULT_TERMINATED_STATES = ["TERMINATED", "DETACHED", "DELETED"]

ACTION_IDEMPOTENT_STATES = {
    "START": DEFAULT_READY_STATES,
    "STOP": ["STOPPED"],
    "SOFTSTOP": ["STOPPED"],
    "DISABLE": ["DISABLED"],
    "ENABLE": ["ENABLED"],
    "CANCEL_KEY_DELETION": DEFAULT_READY_STATES,
    "CANCEL_KEY_VERSION_DELETION": DEFAULT_READY_STATES,
    "CANCEL_VAULT_DELETION": DEFAULT_READY_STATES,
    "CANCEL_SECRET_DELETION": DEFAULT_READY_STATES,
    "CANCEL": CANCELLED_STATES,
    "DEACTIVATE": ["INACTIVE"],
    "ACTIVATE": ["ACTIVE"],
}

ACTION_DESIRED_STATES = {
    "START": DEFAULT_READY_STATES,
    "STOP": ["STOPPED"],
    "SOFTRESET": DEFAULT_READY_STATES,
    "RESET": DEFAULT_READY_STATES,
    "SOFTSTOP": ["STOPPED"],
    "DISABLE": ["DISABLED"],
    "ENABLE": ["ENABLED"],
    "SCHEDULE_KEY_DELETION": DEAD_STATES,
    "CANCEL_KEY_DELETION": DEFAULT_READY_STATES,
    "SCHEDULE_KEY_VERSION_DELETION": DEAD_STATES,
    "CANCEL_KEY_VERSION_DELETION": DEFAULT_READY_STATES,
    "SCHEDULE_VAULT_DELETION": DEAD_STATES,
    "CANCEL_VAULT_DELETION": DEFAULT_READY_STATES,
    "SCHEDULE_SECRET_DELETION": DEAD_STATES,
    "CANCEL_SECRET_DELETION": DEFAULT_READY_STATES,
    "CANCEL": CANCELLED_STATES,
    "DEACTIVATE": ["INACTIVE"],
    "ACTIVATE": ["ACTIVE"],
}

ALWAYS_PERFORM_ACTIONS = ["RESET", "SOFTRESET", "EXPORT", "DETECT_STACK_DRIFT"]

RESOURCE_TYPE_TO_ENTITY_TYPE_MAP = {
    "http_redirect": "redirect",
}

CREATE_OPERATION_KEY = "CREATE"
UPDATE_OPERATION_KEY = "UPDATE"
PATCH_OPERATION_KEY = "PATCH"
DELETE_OPERATION_KEY = "DELETE"
ACTION_OPERATION_KEY = "ACTION"
ANY_OPERATION_KEY = "ANY"

MEBIBYTE = 1024 * 1024


def call_with_backoff(fn, *args, **kwargs):
    if "retry_strategy" not in kwargs:
        kwargs["retry_strategy"] = DEFAULT_RETRY_STRATEGY
    try:
        return fn(*args, **kwargs)
    except TypeError as te:
        if "unexpected keyword argument" in str(te):
            # to handle older SDKs that did not support retry_strategy
            del kwargs["retry_strategy"]
            return fn(*args, **kwargs)
        else:
            # A validation error raised by the SDK, throw it back
            raise


def filter_resources(all_resources, filter_params):
    if not filter_params:
        return all_resources
    return [
        resource
        for resource in all_resources
        if all(
            [
                getattr(resource, key, None) == value
                for key, value in six.iteritems(filter_params)
            ]
        )
    ]


def filter_response_data(response_data, filter_params):
    if not filter_params:
        return response_data
    if isinstance(response_data, oci.dns.models.RecordCollection) or isinstance(
        response_data, oci.dns.models.RRSet
    ):
        return response_data.__class__(
            items=filter_resources(response_data.items, filter_params)
        )
    if isinstance(response_data, oci.object_storage.models.ListObjects):
        return response_data.__class__(
            objects=filter_resources(response_data.objects, filter_params)
        )
    return filter_resources(response_data, filter_params)


def list_all_resources(target_fn, **kwargs):
    """
    Return all resources after paging through all results returned by target_fn. If a `display_name` or `name` is
    provided as a kwarg, then only resources matching the specified name are returned.
    :param target_fn: The target OCI SDK paged function to call
    :param kwargs: All arguments that the OCI SDK paged function expects
    :return: List of all objects returned by target_fn
    :raises ServiceError: When the Service returned an Error response
    :raises MaximumWaitTimeExceededError: When maximum wait time is exceeded while invoking target_fn
    """
    filter_params = None
    try:
        response = oci.pagination.list_call_get_all_results(target_fn, **kwargs)
    except ValueError as ex:
        if "unknown kwargs" in str(ex):
            if "display_name" in kwargs:
                if kwargs["display_name"]:
                    filter_params = {"display_name": kwargs["display_name"]}
                del kwargs["display_name"]
            elif "name" in kwargs:
                if kwargs["name"]:
                    filter_params = {"name": kwargs["name"]}
                del kwargs["name"]
        response = oci.pagination.list_call_get_all_results(target_fn, **kwargs)

    # If the underlying SDK Service list* method doesn't support filtering by name or display_name, filter the resources
    # and return the matching list of resources
    return filter_response_data(response.data, filter_params)


# compare_dicts is used to compare create and update model dicts with the existing resource. Since the existing
# resource might have more parameters (for ex: OCID, time_created etc) than the information we provide during the
# creation, we do a subset match of the dictionary.
# But if a parameter present in the create/update model and not in existing resource, it is considered a mismatch by default
# This behaviour can be changed by setting the flag `ignore_attr_if_not_in_target`.
def compare_dicts(
    source_dict,
    target_dict,
    attrs=None,
    ignore_attr_if_not_in_target=False,
    exclude_attributes=None,
    stack=None,
):
    if exclude_attributes is None:
        exclude_attributes = []
    if stack is None:
        stack = []
    if source_dict is None:
        _debug("dict is not subset because source dict is None")
        return False

    if target_dict is None:
        _debug("dict is not subset because target dict is None")
        return False

    if not isinstance(source_dict, dict):
        _debug("dict is not subset because source_dict is not a dict")
        return False

    if not isinstance(target_dict, dict):
        _debug("dict is not subset because target_dict is not a dict")
        return False

    # handle the case when source dict is empty but target dict has values
    if not source_dict and target_dict:
        _debug("dicts are not equal because source dict is empty and target is not")
        return False
    if not attrs:
        attrs = list(source_dict)
    for attr in attrs:
        stack.append(attr)
        if is_any_key_matching_stack(exclude_attributes, stack):
            stack.pop()
            continue
        # compare attributes if it is only in source dict
        if attr not in source_dict or source_dict.get(attr) is None:
            stack.pop()
            continue
        if attr not in target_dict:
            if ignore_attr_if_not_in_target:
                # if the ignore parameter is set, ignore this attribute.
                # This might be useful in cases where some of the attributes used in create
                # are not exposed in the get model
                stack.pop()
                continue
            _debug(
                "dict is not subset because attribute '{attr}' is not in target dict".format(
                    attr=attr
                )
            )
            stack.pop()
            return False
        source_val = source_dict.get(attr)
        target_val = target_dict.get(attr)
        if isinstance(source_val, dict):
            if not isinstance(target_val, dict):
                _debug(
                    "dict is not subset because attribute '{attr}' source value is a dict and target value is not".format(
                        attr=attr
                    )
                )
                stack.pop()
                return False
            if not compare_dicts(
                source_val,
                target_val,
                ignore_attr_if_not_in_target=ignore_attr_if_not_in_target,
                exclude_attributes=exclude_attributes,
                stack=stack,
            ):
                stack.pop()
                return False
        elif isinstance(source_val, list):
            if not isinstance(target_val, list):
                _debug(
                    "dict is not subset because attribute '{attr}' source value is list and target value is not".format(
                        attr=attr
                    )
                )
                stack.pop()
                return False
            if not compare_lists(
                source_val,
                target_val,
                exclude_attributes=exclude_attributes,
                stack=stack,
            ):
                stack.pop()
                return False
        elif source_val != target_val:
            if "time" in attr:
                if deserialize_datetime(source_val) == deserialize_datetime(target_val):
                    stack.pop()
                    return True
            _debug(
                "dict is not subset because attribute '{attr}' value in source does not match target".format(
                    attr=attr
                )
            )
            stack.pop()
            return False
        stack.pop()
    return True


def compare_lists(
    source_list,
    target_list,
    ignore_attr_if_not_in_target=False,
    exclude_attributes=None,
    stack=None,
):
    if source_list is None:
        _debug("list is not subset because source list is None")
        return False

    if target_list is None:
        _debug("list is not subset because target list is None")
        return False

    if not isinstance(source_list, list):
        _debug("list is not subset because source list is not a list")
        return False

    if not isinstance(target_list, list):
        _debug("list is not subset because target list is not a list")
        return False

    if len(source_list) != len(target_list):
        _debug(
            "lists are not equal because source length: {source_length} does not match target length: {target_length}".format(
                source_length=len(source_list), target_length=len(target_list)
            )
        )
        return False

    for index, element in enumerate(source_list):
        if not is_in_list(
            target_list,
            element,
            ignore_attr_if_not_in_target=ignore_attr_if_not_in_target,
            exclude_attributes=exclude_attributes,
            stack=stack,
        ):
            _debug(
                "list is not subset because element at index {} in source list, is not present in target list".format(
                    index
                )
            )
            return False

    return True


def is_in_list(
    target_list,
    element,
    ignore_attr_if_not_in_target=False,
    exclude_attributes=None,
    stack=None,
):
    if isinstance(element, dict):
        if any(
            [
                compare_dicts(
                    element,
                    target_element,
                    ignore_attr_if_not_in_target=ignore_attr_if_not_in_target,
                    exclude_attributes=exclude_attributes,
                    stack=stack,
                )
                for target_element in target_list
            ]
        ):
            return True
    elif isinstance(element, list):
        if any(
            [
                compare_lists(
                    element,
                    target_element,
                    ignore_attr_if_not_in_target=ignore_attr_if_not_in_target,
                )
                for target_element in target_list
            ]
        ):
            return True
    else:
        if element in target_list:
            return True

    return False


def get_common_arg_spec(supports_create=False, supports_wait=False):
    """
    Return the common set of module arguments for all OCI cloud modules.
    :param supports_create: Variable to decide whether to add options related to idempotency of create operation.
    :param supports_wait: Variable to decide whether to add options related to waiting for completion.
    :return: A dict with applicable module options.
    """
    # Note: This method is used by most OCI ansible resource modules during initialization. When making changes to this
    # method, ensure that no `oci` python sdk dependencies are introduced in this method. This ensures that the modules
    # can check for absence of OCI Python SDK and fail with an appropriate message. Introducing an OCI dependency in
    # this method would break that error handling logic.
    common_args = dict(
        config_file_location=dict(type="str"),
        config_profile_name=dict(type="str"),
        api_user=dict(type="str"),
        api_user_fingerprint=dict(type="str", no_log=True),
        api_user_key_file=dict(type="str"),
        api_user_key_pass_phrase=dict(type="str", no_log=True),
        auth_type=dict(
            type="str",
            choices=[
                "api_key",
                "instance_principal",
                "instance_obo_user",
                "resource_principal",
            ],
            default="api_key",
        ),
        tenancy=dict(type="str"),
        region=dict(type="str"),
    )

    if supports_create:
        common_args.update(
            key_by=dict(type="list", elements="str", no_log=False),
            force_create=dict(type="bool", default=False),
        )

    if supports_wait:
        common_args.update(
            wait=dict(type="bool", default=True), wait_timeout=dict(type="int"),
        )

    return common_args


def get_result(changed, resource_type, resource=None):
    result = dict(changed=changed)
    result[resource_type] = resource
    return result


def get_resource_state(resource):
    try:
        return resource.lifecycle_state
    except AttributeError:
        return resource["lifecycle_state"]


def get_resource_with_state(resource, state):
    if not resource:
        return resource
    if "lifecycle_state" in resource:
        return dict(resource, lifecycle_state=state)
    return resource


def merge_dicts(*dictionaries):
    """Return a new dictionary by merging all the keys from given dictionaries"""
    merged_dict = dict()
    for dictionary in dictionaries:
        if not dictionary:
            continue
        merged_dict.update(dictionary)
    return merged_dict


def get_default_response_from_resource(resource, headers=None):
    return oci.Response(status=200, headers=headers, data=resource, request=None)


def is_work_request_success(work_request_response):
    return (
        getattr(work_request_response.data, "status", None)
        in WORK_REQUEST_SUCCESS_STATES
    )


def get_work_request_completed_states():
    return WORK_REQUEST_COMPLETED_STATES


def get_work_request_success_states():
    return WORK_REQUEST_SUCCESS_STATES


def raise_does_not_exist_service_error(message=None):
    message = message or "Not authorized or resource does not exist."
    raise ServiceError(
        status=404, code="NotAuthorizedOrNotFound", headers={}, message=message
    )


# convert dictionary to a Python SDK model class
# for example:
#   data: {
#        'hostname_label': 'mytestinstance',
#        'subnet_id': 'ocid1.subnet.oc1.iad.xxxxxEXAMPLExxxxx',
#        'display_name': 'my_vnic'
#   }
#
# model_class: <class 'oci.core.models.create_vnic_details.CreateVnicDetails'>
#
# will create a CreateVnicDetails instance with the relevant fields populated
# based on 'data'
def convert_input_data_to_model_class(data, model_class):
    # e.g. oci.core.models.create_vnic_details.LaunchInstanceDetails -> oci.core.models
    namespace = ".".join(model_class.__module__.split(".")[0:-1])

    # e.g. 'oci.core.models' -> <module 'oci.core.models'>
    module = sys.modules[namespace]

    # if the type is polymoprhic, data might be a subtype of model_class
    # and thus we need to parse it as the correct subtype based on the discriminator
    # if we parse based on the declared (base) type, we will skip all fields that are
    # only defined on the subtype
    model_instance = model_class()
    if hasattr(model_instance, "get_subtype"):
        # get_subtype expects the camelCase version of the data (i.e. if discriminator field
        # name is source_type in python it expects sourceType)
        camelized_top_level_keys = dict(
            (camelize(key), value) for key, value in six.iteritems(data)
        )
        subtype_name = model_instance.get_subtype(camelized_top_level_keys)
        model_class = getattr(module, subtype_name)
        model_instance = model_class()

    for attr in model_instance.attribute_map:
        if data.get(attr) is None:
            continue

        value = data[attr]

        # e.g. LaunchInstanceDetails.swagger_types.get('create_vnic_details') -> 'CreateVnicDetails'
        swagger_type = model_instance.swagger_types.get(attr)
        # if data is complex, we need to convert nested values
        if hasattr(module, swagger_type):
            value = convert_input_data_to_model_class(
                value, getattr(module, swagger_type)
            )
        elif swagger_type.find("list[") == 0:
            # convert individual items in the list to complex type
            element_swagger_type = re.match(r"list\[(.*)\]", swagger_type).group(1)
            if hasattr(module, element_swagger_type):
                converted_values = []
                for element in value:
                    converted_values.append(
                        convert_input_data_to_model_class(
                            element, getattr(module, element_swagger_type)
                        )
                    )
                value = converted_values
        elif swagger_type.find("dict(") == 0:
            # convert individual values in dict to complex type
            match = re.match(r"dict\(([^,]*), (.*)\)", swagger_type)
            entry_value_swagger_type = match.group(2)

            if hasattr(module, entry_value_swagger_type):
                converted_values = {}
                for key in value:
                    converted_values[key] = convert_input_data_to_model_class(
                        value[key], getattr(module, entry_value_swagger_type)
                    )

                value = converted_values

        setattr(model_instance, attr, value)
    return model_instance


# Converts an argument to camel case with a lower case first character. For example
# "my_param" would turn into "myParam" and "this_other_param" would be "thisOtherParam"
#
# Supports both UpperCaseCamel and lowerCaseCamel, though lower case is considered the default
def camelize(to_camelize, uppercase_first_letter=False):
    if not to_camelize:
        return ""

    if uppercase_first_letter:
        return re.sub(r"(?:^|[_-])(.)", lambda m: m.group(1).upper(), to_camelize)
    else:
        return (
            to_camelize[0].lower()
            + camelize(to_camelize, uppercase_first_letter=True)[1:]
        )


def _debug(s):
    logger.debug(s)


def get_logger(module_name):
    oci_logging = setup_logging()
    return oci_logging.getLogger(module_name)


def _httpclient_debug_logging_patch():
    """Enable HTTPConnection debug logging to the logging framework"""

    # we can't patch `http_client.print` the way we need to in python 2 so just skip
    if six.PY2:
        return

    try:
        level = logging.DEBUG
        httpclient_logger = logging.getLogger("http.client")

        def httpclient_log(*args):
            httpclient_logger.log(level, " ".join(args))

        # mask the print() built-in in the http.client module to use
        # logging instead
        # patching the print method is not valid Python 2 syntax so
        # we have to use exec to avoid a SyntaxError when running with
        # python 2
        # (Note: you can only try / except a SyntaxError if it is inside
        # an exec or eval block)
        exec("http_client.print = httpclient_log") in {}

        # enable debugging
        # log_requests MUST be turned on in the config other while the oci python SDK
        # will override the following setting to 0, eliminating http debug logs
        http_client.HTTPConnection.debuglevel = 1
    except Exception:
        # this is best effort to output additional logging, we never want to
        # fail the module if anything in here fails
        pass


def setup_logging(
    default_level="INFO", default_log_path=tempfile.gettempdir(),
):
    """Setup logging configuration"""
    env_log_path = "LOG_PATH"
    env_log_level = "LOG_LEVEL"

    log_path = os.getenv(env_log_path, default_log_path)
    log_level_str = os.getenv(env_log_level, default_level)
    log_format = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
    if log_level_str.lower() == "debug":
        _httpclient_debug_logging_patch()

    log_level = logging.getLevelName(log_level_str)
    # check write access
    log_file_path = os.path.join(log_path, "oci_ansible_module.log")
    if not os.path.exists(log_file_path) or os.access(log_file_path, os.W_OK):
        logging.basicConfig(
            filename=log_file_path, filemode="a", level=log_level, format=log_format
        )
    else:
        # the log file exists but the user does not have write permissions to the file.
        # Disable the logging in this case to avoid failures for now.
        handlers = [logging.NullHandler()]
        logging.basicConfig(level=log_level, format=log_format, handlers=handlers)

    return logging


def pretty_print_json(data):
    return json.dumps(data, indent=2)


def deserialize_datetime(string):
    """
    Deserializes string to datetime.

    The string should be in iso8601 datetime format.

    :param string: str.
    :return: datetime.
    """
    try:
        if not string:
            return string
        if not isinstance(string, six.string_types):
            return string
        date_string_utc = string.replace("+00:00", "Z")
        # If this parser creates a date without raising an exception
        # then the time zone is utc and needs to be set.
        naivedatetime = datetime.strptime(date_string_utc, "%Y-%m-%dT%H:%M:%S.%fZ")
        try:
            from dateutil import tz
        except ImportError:
            return naivedatetime
        else:
            awaredatetime = naivedatetime.replace(tzinfo=tz.tzutc())
            return awaredatetime

    except ValueError:
        try:
            from dateutil.parser import parse

            return parse(date_string_utc)
        except ImportError:
            return string
        except ValueError:
            raise Exception(
                "Incorrect date format `{0}`. It should be YYYY-MM-DD HH:MM:SS".format(
                    string
                )
            )


@contextmanager
def threaded_worker_pool(*args, **kwargs):
    pool = ThreadPool(*args, **kwargs)
    try:
        yield pool
    finally:
        pool.close()
        # wait for all the instances to be processed
        pool.join()
        # terminate the pool
        pool.terminate()


logger = get_logger("oci_common_utils")


def replace_values_in_object_with_stubs(input_object):
    """
    Takes an input object of Any type and returns the
    object with all values in it stubbed out.

    @param: input_object: Any, input object that needs to be stubbed out.
    :returns: Stubbed object with type Optional[Union[List, Dict, str]]
              based on the input type
    """

    if input_object is None:
        return None

    if isinstance(input_object, dict):
        return replace_values_in_dict_with_stubs(input_object)
    elif isinstance(input_object, list):
        return replace_values_in_list_with_stubs(input_object)
    else:
        return "STUBBED_VALUE"


def replace_values_in_list_with_stubs(input_list):
    """
    Takes an input list and replaces all values in the list
    recursively with stubs.
    If the item in list is a list/dict - recurse else stub out.

    @param input_dict: dict, that will be stubbed out for values
    :returns: dict - the stubbed dict
    :raises: TypeError, if input_list is not of type list.
    """

    if input_list is None:
        return input_list

    if not isinstance(input_list, list):
        raise TypeError("input list has unexpected type {}".format(type(input_list)))

    new_list = []
    for item in input_list:
        if isinstance(item, dict):
            new_list.append(replace_values_in_dict_with_stubs(item))
        elif isinstance(item, list):
            new_list.append(replace_values_in_list_with_stubs(item))
        else:
            # for all other types str, bool, int, float etc.
            # we add this explicit string to make sure someone
            # reading the value does not mistake it to be a real value.
            new_list.append("STUBBED_VALUE")

    return new_list


def replace_values_in_dict_with_stubs(input_dict):
    """
    Takes an input dict and replaces all values in the dict
    recursively with stubs.

    @param input_dict: dict, that will be stubbed out for values
    :returns: dict - the stubbed dict
    :raises: TypeError, if input_dict is not of type dict.
    """

    if input_dict is None:
        return input_dict

    if not isinstance(input_dict, dict):
        raise TypeError("input dict has unexpected type {}".format(type(input_dict)))

    for key, value in input_dict.items():
        if isinstance(value, dict):
            input_dict[key] = replace_values_in_dict_with_stubs(value)
        elif isinstance(value, list):
            input_dict[key] = replace_values_in_list_with_stubs(value)
        else:
            # for all other types str, bool, int, float etc.
            # we add this explicit string to make sure someone
            # reading the value does not mistake it to be a real value.
            input_dict[key] = "STUBBED_VALUE"

    return input_dict


def is_any_key_matching_stack(keys, stack):
    if keys is None or stack is None:
        return False
    for key in keys:
        if is_key_matching_stack(key, stack):
            return True
    return False


def is_key_matching_stack(key, stack):
    if key is None or stack is None:
        return False
    key_segments = key.split(".")
    if len(key_segments) != len(stack):
        return False
    for i in range(0, len(key_segments)):
        if key_segments[i] != stack[i]:
            return False
    return True
