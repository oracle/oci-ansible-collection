# Copyright (c) 2020 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type
from ansible.module_utils import six
from ansible.module_utils.six.moves import http_client
from ansible.module_utils._text import to_bytes
from datetime import datetime
import tempfile
import logging
import os
import yaml
import re
import sys
import json

try:
    import oci
    from oci.retry import RetryStrategyBuilder
    from oci.util import to_dict
    from oci.exceptions import ServiceError

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False

MAX_WAIT_TIMEOUT_IN_SECONDS = 1200
DEAD_STATES = [
    "TERMINATING",
    "TERMINATED",
    "FAULTY",
    "FAILED",
    "DELETING",
    "DELETED",
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
    "SUCCEEDED",
    "PENDING_PROVIDER",
]

CANCELLED_STATES = ["CANCELLED"]

WORK_REQUEST_COMPLETED_STATES = ["SUCCEEDED", "SUCCESS", "FAILED", "COMPLETED"]
WORK_REQUEST_SUCCESS_STATES = ["SUCCEEDED", "SUCCESS"]
WORK_REQUEST_FAILED_STATES = ["FAILED"]

# If a resource is in one of these states, it would be considered deleted
DEFAULT_TERMINATED_STATES = ["TERMINATED", "DETACHED", "DELETED"]

ACTION_IDEMPOTENT_STATES = {"START": DEFAULT_READY_STATES, "STOP": ["STOPPED"]}

ACTION_DESIRED_STATES = {
    "START": DEFAULT_READY_STATES,
    "STOP": ["STOPPED"],
    "SOFTRESET": DEFAULT_READY_STATES,
    "RESET": DEFAULT_READY_STATES,
}

ALWAYS_PERFORM_ACTIONS = ["RESET", "SOFTRESET", "EXPORT"]

RESOURCE_TYPE_TO_ENTITY_TYPE_MAP = {"waas_policy": "waas"}

CREATE_OPERATION_KEY = "CREATE"
UPDATE_OPERATION_KEY = "UPDATE"
DELETE_OPERATION_KEY = "DELETE"
ACTION_OPERATION_KEY = "ACTION"
ANY_OPERATION_KEY = "ANY"


def _get_retry_strategy():
    retry_strategy_builder = RetryStrategyBuilder(
        max_attempts_check=True,
        max_attempts=3,
        retry_max_wait_between_calls_seconds=60,
        retry_base_sleep_time_seconds=10,
        backoff_type=oci.retry.BACKOFF_FULL_JITTER_EQUAL_ON_THROTTLE_VALUE,
    )
    retry_strategy_builder.add_service_error_check(
        service_error_retry_config={
            429: [],
            400: ["QuotaExceeded", "LimitExceeded"],
            409: ["Conflict"],
        },
        service_error_retry_on_any_5xx=True,
    )
    return retry_strategy_builder.get_retry_strategy()


def call_with_backoff(fn, *args, **kwargs):
    if "retry_strategy" not in kwargs:
        kwargs["retry_strategy"] = _get_retry_strategy()
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


def is_dict_subset(
    source_dict, target_dict, attrs=None, ignore_attr_if_not_in_target=False
):
    if source_dict is None or target_dict is None:
        _debug(
            "dict is not subset because source_dict: {source_dict} or target dict: {target_dict} is None".format(
                source_dict=source_dict, target_dict=target_dict
            )
        )
        return False
    if not (isinstance(source_dict, dict) and isinstance(target_dict, dict)):
        _debug(
            "dict is not subset because source_dict: {source_dict} or target dict: {target_dict} is not a dict".format(
                source_dict=source_dict, target_dict=target_dict
            )
        )
        return False
    if not attrs:
        attrs = list(source_dict)
    for attr in attrs:
        # compare attributes if it is only in source dict
        if attr not in source_dict or source_dict.get(attr) is None:
            continue
        if attr not in target_dict:
            if ignore_attr_if_not_in_target:
                # if the ignore parameter is set, ignore this attribute.
                # This might be useful in cases where some of the attributes used in create
                # are not exposed in the get model
                continue

            _debug(
                "dict is not subset because attribute '{attr}' is not in target dict".format(
                    attr=attr
                )
            )
            return False
        source_val = source_dict.get(attr)
        target_val = target_dict.get(attr)
        if isinstance(source_val, dict):
            if not isinstance(target_val, dict):
                _debug(
                    "dict is not subset because attribute '{attr}' source value is a dict and target value is not: {target_val}".format(
                        attr=attr, target_val=target_val
                    )
                )
                return False
            if not is_dict_subset(
                source_val,
                target_val,
                ignore_attr_if_not_in_target=ignore_attr_if_not_in_target,
            ):
                return False
        elif isinstance(source_val, list):
            if not isinstance(target_val, list):
                _debug(
                    "dict is not subset because attribute '{attr}' source value is list and target value is not: {target_val}".format(
                        attr=attr, target_val=target_val
                    )
                )
                return False
            if not is_list_subset(source_val, target_val):
                return False
        elif source_val != target_val:
            _debug(
                "dict is not subset because attribute '{attr}' value in source: {source_val} does not match target: {target_val}".format(
                    attr=attr, source_val=source_val, target_val=target_val
                )
            )
            return False
    return True


def is_list_subset(source_list, target_list):
    if source_list is None or target_list is None:
        _debug(
            "list is not subset because source list: {source_list} or target list: {target_list} is None".format(
                source_list=source_list, target_list=target_list
            )
        )
        return False
    if not (isinstance(source_list, list) and isinstance(target_list, list)):
        _debug(
            "list is not subset because source list: {source_list} or target list: {target_list} is not a list".format(
                source_list=source_list, target_list=target_list
            )
        )
        return False
    if all([is_in_list(target_list, element) for element in source_list]):
        return True

    _debug(
        "list is not subset because not all elements in source list are in target list"
    )
    return False


def is_in_list(l, element):
    if isinstance(element, dict):
        if any([is_dict_subset(element, target_element) for target_element in l]):
            return True
    elif isinstance(element, list):
        if any([is_list_subset(element, target_element) for target_element in l]):
            return True
    else:
        if element in l:
            return True

        _debug(
            "element {element} is not in list: {list}".format(element=element, list=l)
        )
    return False


def are_dicts_equal(
    source_dict, target_dict, attrs=None, ignore_attr_if_not_in_target=False
):
    if source_dict is None or target_dict is None:
        _debug(
            "dicts are not equal because source_dict: {source_dict} or target dict: {target_dict} is None".format(
                source_dict=source_dict, target_dict=target_dict
            )
        )
        return False
    if not (isinstance(source_dict, dict) and isinstance(target_dict, dict)):
        _debug(
            "dicts are not equal because source_dict: {source_dict} or target dict: {target_dict} is not a dict".format(
                source_dict=source_dict, target_dict=target_dict
            )
        )
        return False
    if not attrs:
        attrs = list(source_dict)
    # handle the case when source dict is empty but target dict has values
    if not source_dict and target_dict:
        _debug(
            "dicts are not equal because source dict is empty and target is not: {target_dict}".format(
                target_dict=target_dict
            )
        )
        return False
    for attr in attrs:
        # compare attributes if it is only in source dict
        if attr not in source_dict or source_dict.get(attr) is None:
            continue
        if attr not in target_dict:
            if ignore_attr_if_not_in_target:
                # if the ignore parameter is set, ignore this attribute.
                # This might be useful in cases where some of the attributes used in update
                # are not exposed in the get model
                continue

            _debug(
                "dicts are not equal because attribute '{attr}' is not in target dict".format(
                    attr=attr
                )
            )
            return False
        source_val = source_dict.get(attr)
        target_val = target_dict.get(attr)
        if isinstance(source_val, list):
            if not isinstance(target_val, list):
                _debug(
                    "dicts are not equal because attribute '{attr}' source value is a list and target value is not: {target_val}".format(
                        attr=attr, target_val=target_val
                    )
                )
                return False
            if not are_lists_equal(source_val, target_val):
                return False
        elif isinstance(source_val, dict):
            if not isinstance(target_val, dict):
                _debug(
                    "dicts are not equal because attribute '{attr}' source value is a dict and target value is not: {target_val}".format(
                        attr=attr, target_val=target_val
                    )
                )
                return False
            if not are_dicts_equal(
                source_val,
                target_val,
                ignore_attr_if_not_in_target=ignore_attr_if_not_in_target,
            ):
                return False
        elif source_val != target_val:
            _debug(
                "dicts are not equal because attribute '{attr}' value in source: {source_val} does not match target: {target_val}".format(
                    attr=attr, source_val=source_val, target_val=target_val
                )
            )
            return False
    return True


def are_lists_equal(s, t):
    if s is None and t is None:
        return True

    if (s is None and len(t) >= 0) or (t is None and len(s) >= 0):
        _debug(
            "lists are not equal because one of source: {source_val} and target: {target_val} is None and the other is not".format(
                source_val=s, target_val=t
            )
        )
        return False

    if len(s) != len(t):
        _debug(
            "lists are not equal because source length: {source_length} does not match target length: {target_length}".format(
                source_length=len(s), target_length=len(t)
            )
        )
        return False

    if len(s) == 0:
        return True

    s = to_dict(s)
    t = to_dict(t)

    if type(s[0]) == dict:
        # Handle list of dicts. Dictionary returned by the API may have additional keys. For example, a get call on
        # service gateway has an attribute `services` which is a list of `ServiceIdResponseDetails`. This has a key
        # `service_name` which is not provided in the list of `services` by a user while making an update call; only
        # `service_id` is provided by the user in the update call.
        sorted_s = sort_list_of_dictionary(s)
        sorted_t = sort_list_of_dictionary(t)
        for index, d in enumerate(sorted_s):
            if not is_dictionary_subset(d, sorted_t[index]):
                _debug(
                    "lists are not equal because item: {source_item} does not match target item: {target_item}".format(
                        source_item=d, target_item=sorted_t[index]
                    )
                )
                return False
        return True
    else:
        # Handle lists of primitive types.
        try:
            for elem in s:
                t.remove(elem)
        except ValueError:
            _debug(
                "lists are not equal because item '{source_item}' does not exist in target list: {target_list}".format(
                    source_item=elem, target_list=t
                )
            )
            return False
        return not t


def sort_list_of_dictionary(list_of_dict):
    """
    This functions sorts a list of dictionaries. It first sorts each value of the dictionary and then sorts the list of
    individually sorted dictionaries. For sorting, each dictionary's tuple equivalent is used.
    :param list_of_dict: List of dictionaries.
    :return: A sorted dictionary.
    """
    list_with_sorted_dict = []
    for d in list_of_dict:
        sorted_d = sort_dictionary(d)
        list_with_sorted_dict.append(sorted_d)
    return sorted(list_with_sorted_dict, key=get_key_for_comparing_dict)


def is_dictionary_subset(sub, super_dict):
    """
    This function checks if `sub` dictionary is a subset of `super` dictionary.
    :param sub: subset dictionary, for example user_provided_attr_value.
    :param super_dict: super dictionary, for example resources_attr_value.
    :return: True if sub is contained in super.
    """
    # TODO: remove this function or rename it, we shouldn't have is_dictionary_subset and is_dict_subset
    # return is_dict_subset(sub, super_dict)
    for key in sub:
        if sub[key] != super_dict[key]:
            _debug(
                "dictionary is not subset. Value for key '{key}' in subset dict: {subset_val} does not match value in superset dict: {superset_val}".format(
                    key=key, subset_val=sub[key], superset_val=super_dict[key],
                )
            )
            return False
    return True


def sort_dictionary(d):
    """
    This function sorts values of a dictionary recursively.
    :param d: A dictionary.
    :return: Dictionary with sorted elements.
    """
    sorted_d = {}
    for key in d:
        if type(d[key]) == list:
            if d[key] and type(d[key][0]) == dict:
                sorted_value = sort_list_of_dictionary(d[key])
                sorted_d[key] = sorted_value
            else:
                sorted_d[key] = sorted(d[key])
        elif type(d[key]) == dict:
            sorted_d[key] = sort_dictionary(d[key])
        else:
            sorted_d[key] = d[key]
    return sorted_d


def get_key_for_comparing_dict(d):
    tuple_form_of_d = tuplize(d)
    return tuple_form_of_d


def tuplize(d):
    """
    This function takes a dictionary and converts it to a list of tuples recursively.
    :param d: A dictionary.
    :return: List of tuples.
    """
    list_of_tuples = []
    key_list = sorted(list(d.keys()))
    for key in key_list:
        if type(d[key]) == list:
            # Convert a value which is itself a list of dict to a list of tuples.
            if d[key] and type(d[key][0]) == dict:
                sub_tuples = []
                for sub_dict in d[key]:
                    sub_tuples.append(tuplize(sub_dict))
                # To handle comparing two None values, while creating a tuple for a {key: value}, make the first element
                # in the tuple a boolean `True` if value is None so that attributes with None value are put at last
                # in the sorted list.
                list_of_tuples.append((sub_tuples is None, key, sub_tuples))
            else:
                list_of_tuples.append((d[key] is None, key, d[key]))
        elif type(d[key]) == dict:
            tupled_value = tuplize(d[key])
            list_of_tuples.append((tupled_value is None, key, tupled_value))
        else:
            list_of_tuples.append((d[key] is None, key, d[key]))
    return list_of_tuples


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
            type="str", choices=["api_key", "instance_principal"], default="api_key"
        ),
        tenancy=dict(type="str"),
        region=dict(type="str"),
    )

    if supports_create:
        common_args.update(
            key_by=dict(type="list"), force_create=dict(type="bool", default=False)
        )

    if supports_wait:
        common_args.update(
            wait=dict(type="bool", default=True),
            wait_timeout=dict(type="int", default=MAX_WAIT_TIMEOUT_IN_SECONDS),
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


def get_entity_type(resource_type):
    if not resource_type:
        return resource_type
    if resource_type in RESOURCE_TYPE_TO_ENTITY_TYPE_MAP:
        return RESOURCE_TYPE_TO_ENTITY_TYPE_MAP[resource_type]
    return resource_type.strip().replace("_", "")


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
    default_config_file="/etc/ansible/oci_logging.yaml",
    default_level="INFO",
    default_log_path=tempfile.gettempdir(),
):
    """Setup logging configuration"""
    env_config_file = "LOG_CONFIG"
    env_log_path = "LOG_PATH"
    env_log_level = "LOG_LEVEL"

    config_file = os.getenv(env_config_file, default_config_file)
    log_path = os.getenv(env_log_path, default_log_path)

    files_handlers = ["debug_file_handler", "error_file_handler", "info_file_handler"]

    if os.path.exists(config_file):
        with open(to_bytes(config_file), "rt") as f:
            config = yaml.safe_load(f.read())
            for files_handler in files_handlers:
                config["handlers"][files_handler]["filename"] = config["handlers"][
                    files_handler
                ]["filename"].format(
                    path=log_path, date=datetime.today().strftime("%d-%m-%Y")
                )
        logging.config.dictConfig(config)
    else:
        log_level_str = os.getenv(env_log_level, default_level)

        if log_level_str.lower() == "debug":
            _httpclient_debug_logging_patch()

        log_level = logging.getLevelName(log_level_str)

        log_file_path = os.path.join(log_path, "oci_ansible_module.log")

        logging.basicConfig(filename=log_file_path, filemode="a", level=log_level)
    return logging


def pretty_print_json(data):
    return json.dumps(data, indent=2)


logger = get_logger("oci_common_utils")
