# Copyright (c) 2018, 2019 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from ansible.module_utils.oracle import oci_utils
from ansible.module_utils import six
from ansible.module_utils.facts.utils import get_file_content

try:
    import oci
    from oci.load_balancer.models import (
        BackendDetails,
        BackendSetDetails,
        HealthCheckerDetails,
        SessionPersistenceConfigurationDetails,
        SSLConfigurationDetails,
        CertificateDetails,
        ListenerDetails,
        ConnectionConfiguration,
        PathRouteSetDetails,
        PathRoute,
        PathMatchType,
        HostnameDetails,
        CreateCertificateDetails,
    )
    from oci.util import to_dict
    from oci.exceptions import ServiceError, ClientError, MaximumWaitTimeExceeded

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False

DEFAULT_COMPLETED_STATES = ["SUCCEEDED", "FAILED"]

MAX_WAIT_TIMEOUT_IN_SECONDS = 1200

logger = oci_utils.get_logger("oci_lb_utils")


def verify_work_request(lb_client, response):
    work_request_id = None
    if response is not None:
        work_request_id = response.headers.get("opc-work-request-id")
    oci.wait_until(
        lb_client,
        lb_client.get_work_request(work_request_id),
        evaluate_response=lambda r: r.data.lifecycle_state in ["SUCCEEDED", "FAILED"],
    )
    response = lb_client.get_work_request(work_request_id)
    if response.data.lifecycle_state == "FAILED":
        raise ClientError(Exception(response.data.error_details))
    return response


def create_or_update_lb_resources_and_wait(
    lb_client,
    resource_type,
    function,
    kwargs_function,
    module,
    get_fn=None,
    get_sub_resource_fn=None,
    get_param=None,
    states=None,
    wait_applicable=True,
    kwargs_get=None,
):
    result = dict()
    result[resource_type] = dict()
    try:
        response = oci_utils.call_with_backoff(function, **kwargs_function)
        work_request_id = response.headers.get("opc-work-request-id")
        if wait_applicable and module.params.get("wait", None):
            if states is None:
                states = module.params.get("wait_until") or DEFAULT_COMPLETED_STATES
            response = get_work_request_response(
                lb_client, work_request_id, states, module
            )
            if response.data.lifecycle_state == "FAILED":
                module.fail_json(msg=response.data.error_details)

            if kwargs_get:
                if get_sub_resource_fn:
                    result[resource_type] = to_dict(get_sub_resource_fn(**kwargs_get))
                else:
                    result[resource_type] = to_dict(
                        oci_utils.call_with_backoff(get_fn, **kwargs_get).data
                    )
            else:
                result[resource_type] = to_dict(
                    oci_utils.call_with_backoff(
                        get_fn, **{get_param: to_dict(response.data).get(get_param)}
                    ).data
                )
        result["changed"] = True
    except ServiceError as ex:
        logger.error("Unable to create/update %s due to: %s", resource_type, ex.message)
        module.fail_json(msg=ex.message)
    except MaximumWaitTimeExceeded as ex:
        logger.error("Unable to create/update %s due to: %s", resource_type, str(ex))
        module.fail_json(msg=str(ex))
    return result


def delete_lb_resources_and_wait(
    lb_client,
    resource_type,
    function,
    kwargs_function,
    module,
    get_fn=None,
    get_sub_resource_fn=None,
    get_param=None,
    states=None,
    wait_applicable=True,
    kwargs_get=None,
):
    result = dict(changed=False)
    try:
        if get_sub_resource_fn:
            resource = to_dict(get_sub_resource_fn(**kwargs_get))
        else:
            resource = to_dict(oci_utils.call_with_backoff(get_fn, **kwargs_get).data)

        if resource:
            result[resource_type] = resource
            response = oci_utils.call_with_backoff(function, **kwargs_function)
            work_request_id = response.headers.get("opc-work-request-id")
            if wait_applicable and module.params.get("wait", None):
                if states is None:
                    states = module.params.get("wait_until") or DEFAULT_COMPLETED_STATES

            response = get_work_request_response(
                lb_client, work_request_id, states, module
            )
            if response.data.lifecycle_state == "FAILED":
                module.fail_json(msg=response.data.error_details)
            result["changed"] = True
        else:
            result[resource_type] = dict()
    except MaximumWaitTimeExceeded as ex:
        module.fail_json(msg=str(ex))
    except ServiceError as ex:
        if ex.status != 404:
            module.fail_json(msg=ex.message)
        result[resource_type] = dict()
    return result


def get_work_request_response(lb_client, work_request_id, states, module):
    work_request_response = oci_utils.call_with_backoff(
        lb_client.get_work_request, work_request_id=work_request_id
    )
    response = oci.wait_until(
        lb_client,
        work_request_response,
        evaluate_response=lambda r: r.data.lifecycle_state in states,
        max_wait_seconds=module.params.get("wait_timeout", MAX_WAIT_TIMEOUT_IN_SECONDS),
    )
    return response


def get_backend_name(module):
    return module.params["ip_address"] + ":" + str(module.params["port"])


def get_existing_load_balancer(lb_client, module, load_balancer_id):
    existing_lb = None
    if load_balancer_id is None:
        raise ClientError(
            Exception(
                "load_balancer_id is mandatory for update and delete use cases \
                      and must not be empty"
            )
        )
    try:
        response = lb_client.get_load_balancer(load_balancer_id)
        existing_lb = response.data
    except ServiceError as ex:
        if ex.status != 404:
            module.fail_json(msg=ex.message)
    return existing_lb


def create_listeners(listener_details_dict):
    if listener_details_dict is None:
        return None
    result_listeners = dict()
    attributes = [
        "default_backend_set_name",
        "port",
        "protocol",
        "hostname_names",
        "path_route_set_name",
    ]
    optional_attributes = ["hostname_names", "path_route_set_name"]
    for key, value in six.iteritems(listener_details_dict):
        listener_details = ListenerDetails()
        for attribute in attributes:
            if value.get(attribute) is None and attribute not in optional_attributes:
                raise ClientError(
                    Exception(
                        attribute + " is mandatory and must not be empty for listener"
                    )
                )
            listener_details.__setattr__(attribute, value.get(attribute))
        listener_details.ssl_configuration = create_ssl_configuration(
            value.get("ssl_configuration", None)
        )
        listener_details.connection_configuration = create_connection_configuration(
            value.get("connection_configuration", None)
        )
        result_listeners.update({key: listener_details})
    return result_listeners


def create_certificates(certificate_details_dict):
    if certificate_details_dict is None:
        return None
    result_certificates = dict()
    attributes = ["ca_certificate", "private_key", "public_certificate"]
    for key, value in six.iteritems(certificate_details_dict):
        certificate_details = CertificateDetails()
        certificate_name = value.get("certificate_name")
        if certificate_name is None:
            raise ClientError(
                Exception(
                    "certificate_name is mandatory and must not be empty for certificate creation"
                )
            )
        certificate_details.certificate_name = certificate_name
        certificate_details.passphrase = value.get("passphrase", None)
        for attribute in attributes:
            if value.get(attribute) is not None:
                certificate_details.__setattr__(
                    attribute, get_file_content(value.get(attribute, None))
                )
        result_certificates.update({key: certificate_details})
    return result_certificates


def create_backend_sets(backend_sets_dicts):
    if backend_sets_dicts is None:
        return None
    result_backend_sets = dict()
    for key, value in six.iteritems(backend_sets_dicts):
        backend_sets_details = BackendSetDetails()
        health_checker = value.get("health_checker", None)
        policy = value.get("policy", None)
        if health_checker is None or policy is None:
            raise ClientError(
                Exception(
                    "health_checker and policy are mandatory attributes for back_end_sets and can not be empty."
                )
            )
        backend_sets_details.policy = value["policy"]
        backend_sets_details.health_checker = create_health_checker(health_checker)
        backend_sets_details.backends = create_backends(value.get("backends", None))
        backend_sets_details.session_persistence_configuration = create_session_persistence_configuration(
            value.get("session_persistence_configuration", None)
        )
        backend_sets_details.ssl_configuration = create_ssl_configuration(
            value.get("ssl_configuration", None)
        )
        result_backend_sets.update({key: backend_sets_details})
    return result_backend_sets


def create_backends(backends_list):
    if backends_list is None:
        return None
    result_backends = list()
    attribute_to_default_value_dict = dict(
        {"backup": False, "drain": False, "offline": False, "weight": 1}
    )
    HashedBackendDetails = oci_utils.generate_subclass(BackendDetails)
    for backend_entry in backends_list:
        backend = HashedBackendDetails()
        ip_address = backend_entry.get("ip_address", None)
        port = backend_entry.get("port", None)
        if ip_address is None or port is None:
            raise ClientError(
                Exception(
                    "ip_address and port are mandatory attributes for back_ends and can not "
                    "be empty."
                )
            )
        backend.ip_address = ip_address
        backend.port = port
        for key, value in six.iteritems(attribute_to_default_value_dict):
            backend.__setattr__(key, backend_entry.get(key, value))
        result_backends.append(backend)
    return result_backends


def create_health_checker(health_checker_details):
    if health_checker_details is None:
        return None
    HashedHealthCheckerDetails = oci_utils.generate_subclass(HealthCheckerDetails)
    health_checker = HashedHealthCheckerDetails()
    attribute_to_default_value_dict = dict(
        {
            "interval_in_millis": 10000,
            "port": 0,
            "response_body_regex": ".*",
            "retries": 3,
            "return_code": 200,
            "timeout_in_millis": 3000,
        }
    )
    protocol = health_checker_details.get("protocol", None)
    url_path = health_checker_details.get("url_path", None)
    if protocol is None or url_path is None:
        raise ClientError(
            Exception(
                "protocol and url_path are mandatory attributes for health_checker and can not be empty."
            )
        )
    health_checker.protocol = protocol
    health_checker.url_path = url_path
    for key, value in six.iteritems(attribute_to_default_value_dict):
        health_checker.__setattr__(key, health_checker_details.get(key, value))
    return health_checker


def create_session_persistence_configuration(session_persistence_configuration):
    if session_persistence_configuration is None:
        return None
    HashedSessionPersistenceConfigurationDetails = oci_utils.generate_subclass(
        SessionPersistenceConfigurationDetails
    )
    result_session_persistence_configuration = (
        HashedSessionPersistenceConfigurationDetails()
    )
    cookie_name = session_persistence_configuration.get("cookie_name")
    if cookie_name is None:
        raise ClientError(
            Exception(
                "cookie_name is mandatory attributes for session_persistence_configuration and can not be empty."
            )
        )
    result_session_persistence_configuration.cookie_name = cookie_name
    result_session_persistence_configuration.disable_fallback = session_persistence_configuration.get(
        "disable_fallback", False
    )
    return result_session_persistence_configuration


def create_ssl_configuration(ssl_configuration_details):
    if ssl_configuration_details is None:
        return None
    HashedSSLConfigurationDetails = oci_utils.generate_subclass(SSLConfigurationDetails)
    result_ssl_configuration = HashedSSLConfigurationDetails()
    attributes = ["verify_depth", "verify_peer_certificate"]
    certificate_name = ssl_configuration_details.get("certificate_name")
    if certificate_name is None:
        raise ClientError(
            Exception(
                "certificate_name is mandatory attributes for ssl_configuration and can not be empty."
            )
        )
    result_ssl_configuration.certificate_name = certificate_name
    for attribute in attributes:
        result_ssl_configuration.__setattr__(
            attribute, ssl_configuration_details.get(attribute)
        )
    return result_ssl_configuration


def create_connection_configuration(connection_configuration_details):
    if connection_configuration_details is None:
        return None
    HashedConnectionConfiguration = oci_utils.generate_subclass(ConnectionConfiguration)
    result_connection_configuration = HashedConnectionConfiguration()
    idle_timeout = connection_configuration_details.get("idle_timeout")
    if idle_timeout is None:
        raise ClientError(
            Exception(
                "idle_timeout is mandatory attributes for connection_configuration and can not be empty."
            )
        )
    result_connection_configuration.idle_timeout = idle_timeout
    return result_connection_configuration


def create_path_route_sets(path_route_sets_dicts):
    if path_route_sets_dicts is None:
        return None
    result_path_route_sets = dict()
    for key, value in six.iteritems(path_route_sets_dicts):
        path_route_sets_details = PathRouteSetDetails()
        path_route_sets_details.path_routes = create_path_routes(
            value.get("path_routes", None)
        )
        result_path_route_sets.update({key: path_route_sets_details})
    return result_path_route_sets


def create_path_routes(path_routes_list):
    if path_routes_list is None:
        raise ClientError(
            "path_routes is mandatory attribute for path_route_set and can not be empty."
        )
    HashedPathMatchType = oci_utils.generate_subclass(PathMatchType)
    path_match_type = dict(
        EXACT_MATCH=HashedPathMatchType(
            match_type=PathMatchType.MATCH_TYPE_EXACT_MATCH
        ),
        FORCE_LONGEST_PREFIX_MATCH=HashedPathMatchType(
            match_type=PathMatchType.MATCH_TYPE_FORCE_LONGEST_PREFIX_MATCH
        ),
        PREFIX_MATCH=HashedPathMatchType(
            match_type=PathMatchType.MATCH_TYPE_PREFIX_MATCH
        ),
        SUFFIX_MATCH=HashedPathMatchType(
            match_type=PathMatchType.MATCH_TYPE_SUFFIX_MATCH
        ),
    )
    result_path_routes = list()
    HashedPathRoute = oci_utils.generate_subclass(PathRoute)
    for path_route_entry in path_routes_list:
        path_route = HashedPathRoute()
        backend_set_name = path_route_entry.get("backend_set_name", None)
        path = path_route_entry.get("path", None)
        path_match_type = path_match_type.get(
            path_route_entry.get("path_match_type", None).get("match_type", None)
        )
        if backend_set_name is None or path is None or path_match_type is None:
            raise ClientError(
                Exception(
                    "backend_set_name, path and path_match_type are mandatory attributes for"
                    " back_ends and can not be empty."
                )
            )
        path_route.backend_set_name = backend_set_name
        path_route.path = path
        path_route.path_match_type = path_match_type
        result_path_routes.append(path_route)
    return result_path_routes


def create_hostnames(hostnames_dicts):
    if hostnames_dicts is None:
        return None
    result_hostnames = dict()
    for key, value in six.iteritems(hostnames_dicts):
        hostname_details = HostnameDetails()
        name = value.get("name", None)
        hostname = value.get("hostname", None)
        if name is None or hostname is None:
            raise ClientError(
                Exception(
                    "name and hostname are mandatory attributes for hostnames and can not be empty."
                )
            )
        hostname_details.name = name
        hostname_details.hostname = hostname
        result_hostnames.update({key: hostname_details})
    return result_hostnames


def get_listener(**kwargs_get_listener):
    listener = ""
    lb_client = kwargs_get_listener.get("lb_client")
    module = kwargs_get_listener.get("module")
    lb_id = kwargs_get_listener.get("load_balancer_id")
    name = kwargs_get_listener.get("name")
    existing_load_balancer = to_dict(
        oci_utils.get_existing_resource(
            lb_client.get_load_balancer, module, load_balancer_id=lb_id
        )
    )
    if existing_load_balancer is None:
        module.fail_json(msg="Load balancer with id: " + lb_id + " does not exist")
    if name in existing_load_balancer.get("listeners"):
        listener = existing_load_balancer["listeners"][name]
    return listener


def get_certificate(lb_client, module, lb_id, name):
    existing_certificate = None
    logger.debug("Trying to get Certificate %s in Load Balancer %s", name, lb_id)
    try:
        response = oci_utils.call_with_backoff(
            lb_client.list_certificates, load_balancer_id=lb_id
        )
        certificates = response.data
        certificate = next(
            (
                certificate
                for certificate in certificates
                if certificate.certificate_name == name
            ),
            None,
        )
        if certificate:
            existing_certificate = certificate
    except ServiceError as ex:
        logger.error("Failed to perform checking existing Certificates", exc_info=True)
        module.fail_json(msg=ex.message)
    if existing_certificate is None:
        logger.debug("Certificate %s does not exist in load balancer %s", name, lb_id)
    return existing_certificate


def get_create_certificate_details(module, name):
    certificate_input_details = dict(
        {
            "certificate_name": name,
            "ca_certificate": module.params.get("ca_certificate"),
            "passphrase": module.params.get("passphrase"),
            "private_key": module.params.get("private_key"),
            "public_certificate": module.params.get("public_certificate"),
        }
    )
    certificate_details = create_certificates(
        dict({name: certificate_input_details})
    ).get(name)
    create_certificate_details = CreateCertificateDetails()
    for attribute in create_certificate_details.attribute_map:
        create_certificate_details.__setattr__(
            attribute, getattr(certificate_details, attribute)
        )
    return create_certificate_details


def is_same_certificate(create_certificate_details, certificate):
    same_certificate = True
    if next(
        (
            attribute
            for attribute in certificate.attribute_map
            if getattr(certificate, attribute)
            != getattr(create_certificate_details, attribute)
        ),
        None,
    ):
        same_certificate = False
    return same_certificate


def generic_hash(obj):
    """
    Compute a hash of all the fields in the object
    :param obj: Object whose hash needs to be computed
    :return: a hash value for the object
    """
    sum = 0
    for field in obj.attribute_map.keys():
        sum = sum + hash(getattr(obj, field))
    return sum


def generic_eq(s, other):
    if other is None:
        return False
    return s.__dict__ == other.__dict__


def generate_subclass(parent_class):
    """Make a class hash-able by generating a subclass with a __hash__ method that returns the sum of all fields within
    the parent class"""
    dict_of_method_in_subclass = {
        "__init__": parent_class.__init__,
        "__hash__": generic_hash,
        "__eq__": generic_eq,
    }
    subclass_name = "GeneratedSub" + parent_class.__name__
    generated_sub_class = type(
        subclass_name, (parent_class,), dict_of_method_in_subclass
    )
    return generated_sub_class
