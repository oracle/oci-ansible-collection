# Copyright (c) 2018, 2019, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from ansible.module_utils.oracle import oci_utils

try:
    import oci
    from oci.container_engine.models import KeyValue
    from oci.util import to_dict
    from oci.exceptions import ServiceError, MaximumWaitTimeExceeded

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


MAX_WAIT_TIMEOUT_IN_SECONDS = 1200

DEFAULT_READY_STATES = [
    "AVAILABLE",
    "ACTIVE",
    "RUNNING",
    "PROVISIONED",
    "ATTACHED",
    "ASSIGNED",
]

DEFAULT_TERMINATED_STATES = ["TERMINATED", "DETACHED", "DELETED"]

FAILED_STATES = ["FAILED"]

logger = oci_utils.get_logger("oci_ce_utils")


def _debug(s):
    get_logger().debug(s)


def get_logger():
    return logger


def wait_on_work_request(client, response, module):
    try:
        if module.params.get("wait", None):
            wait_response = oci.wait_until(
                client,
                response,
                evaluate_response=lambda r: r.data.status == "SUCCEEDED",
                max_wait_seconds=module.params.get(
                    "wait_timeout", MAX_WAIT_TIMEOUT_IN_SECONDS
                ),
            )
        else:
            wait_response = oci.wait_until(
                client,
                response,
                evaluate_response=lambda r: r.data.status == "ACCEPTED",
                max_wait_seconds=module.params.get(
                    "wait_timeout", MAX_WAIT_TIMEOUT_IN_SECONDS
                ),
            )
    except MaximumWaitTimeExceeded as ex:
        module.fail_json(msg=str(ex))
    except ServiceError as ex:
        module.fail_json(msg=str(ex))
    return wait_response.data


def wait_on_resource(
    client, module, get_fn, kwargs_get, states, evaluate_response=None
):
    try:
        if evaluate_response:
            wait_response = oci.wait_until(
                client,
                get_fn(**kwargs_get),
                evaluate_response=evaluate_response,
                max_wait_seconds=module.params.get(
                    "wait_timeout", MAX_WAIT_TIMEOUT_IN_SECONDS
                ),
            )
        else:
            wait_response = oci.wait_until(
                client,
                get_fn(**kwargs_get),
                evaluate_response=lambda r: not hasattr(r.data, "lifecycle_state")
                or r.data.lifecycle_state in states,
                max_wait_seconds=module.params.get(
                    "wait_timeout", MAX_WAIT_TIMEOUT_IN_SECONDS
                ),
            )
        return wait_response.data
    except MaximumWaitTimeExceeded as ex:
        module.fail_json(msg=str(ex))
    except ServiceError as ex:
        module.fail_json(msg=str(ex))


def delete_and_wait(
    resource_type,
    client,
    get_fn,
    kwargs_get,
    delete_fn,
    kwargs_delete,
    module,
    states=None,
    wait_applicable=True,
):
    result = dict(changed=False)
    try:
        resource = ""
        resource = to_dict(oci_utils.call_with_backoff(get_fn, **kwargs_get).data)
        if resource:
            if resource_type == "work_request":
                if resource["status"] not in ["CANCELING", "CANCELED"]:
                    resource = call_and_wait(
                        client,
                        result,
                        wait_applicable,
                        module,
                        states,
                        DEFAULT_TERMINATED_STATES,
                        delete_fn,
                        kwargs_delete,
                        get_fn,
                        kwargs_get,
                        evaluate_response=lambda r: r.data.status
                        in ["CANCELING", "CANCELED"],
                    )
            elif "lifecycle_state" not in resource or resource[
                "lifecycle_state"
            ] not in ["DELETING", "DELETED"]:
                resource = call_and_wait(
                    client,
                    result,
                    wait_applicable,
                    module,
                    states,
                    DEFAULT_TERMINATED_STATES,
                    delete_fn,
                    kwargs_delete,
                    get_fn,
                    kwargs_get,
                )
            result[resource_type] = resource
        else:
            _debug(
                "Resource {0} with {1} already deleted. So returning changed=False".format(
                    resource_type, kwargs_get
                )
            )
    except ServiceError as ex:
        if ex.status != 404:
            module.fail_json(msg=ex.message)
        result[resource_type] = resource
    return result


def call_and_wait(
    client,
    result,
    wait_applicable,
    module,
    states,
    default_states,
    fn,
    kwargs_fn,
    get_fn,
    kwargs_get,
    evaluate_response=None,
):
    # Get the resource as after a delete operation on a resource(eg node pool) the resource may not exist.
    resource = to_dict(oci_utils.call_with_backoff(get_fn, **kwargs_get).data)
    wr_id = oci_utils.call_with_backoff(fn, **kwargs_fn).headers.get(
        "opc-work-request-id"
    )
    if wr_id:
        get_wr_response = oci_utils.call_with_backoff(
            client.get_work_request, work_request_id=wr_id
        )
        result["work_request"] = to_dict(
            wait_on_work_request(client, get_wr_response, module)
        )
    result["changed"] = True
    if wait_applicable and module.params.get("wait", None):
        if states is None:
            states = module.params.get("wait_until") or default_states
        resource = to_dict(
            wait_on_resource(
                client, module, get_fn, kwargs_get, states, evaluate_response
            )
        )
    else:
        try:
            resource = to_dict(oci_utils.call_with_backoff(get_fn, **kwargs_get).data)
        except ServiceError as ex:
            if ex.status != 404:
                module.fail_json(msg=ex.message)
    return resource


def update_and_wait(
    resource_type,
    client,
    get_fn,
    kwargs_get,
    update_fn,
    primitive_params_update,
    kwargs_non_primitive_update,
    module,
    update_attributes,
    states=None,
    wait_applicable=True,
):
    try:
        result = dict(changed=False)
        attributes_to_update, resource = oci_utils.get_attr_to_update(
            get_fn, kwargs_get, module, update_attributes
        )
        if attributes_to_update:
            kwargs_update = oci_utils.get_kwargs_update(
                attributes_to_update,
                kwargs_non_primitive_update,
                module,
                primitive_params_update,
            )
            if resource_type == "node_pool":
                # UpdateNodePoolDetails has a non-primitive type 'initial_node_labels'.
                set_node_pool_kwargs_update(kwargs_update, module)
            resource = call_and_wait(
                client,
                result,
                wait_applicable,
                module,
                states,
                DEFAULT_READY_STATES,
                update_fn,
                kwargs_update,
                get_fn,
                kwargs_get,
            )
            # Wait for specified number of nodes to be ACTIVE after update operation.
            if resource_type == "node_pool":
                resource = wait_for_nodes(
                    module, client, get_fn, "node_pool_id", resource["id"]
                )
        result[resource_type] = to_dict(resource)
        return result
    except ServiceError as ex:
        module.fail_json(msg=ex.message)


def set_node_pool_kwargs_update(kwargs_update, module):
    node_labels = module.params["initial_node_labels"]
    if node_labels:
        initial_node_labels = []
        for d in node_labels:
            if d.get("key", None) and d.get("value", None):
                keyvalue = KeyValue()
                keyvalue.key = d.get("key")
                keyvalue.value = d.get("value")
                initial_node_labels.append(keyvalue)
        kwargs_update[
            "update_node_pool_details"
        ].initial_node_labels = initial_node_labels
    return kwargs_update


def wait_for_nodes(module, client, get_fn, get_param, node_pool_id):
    state_to_wait_for = module.params["wait_until"] or "ACTIVE"
    count_of_nodes_to_wait = module.params["count_of_nodes_to_wait"]

    def check_nodes(response):
        nodes_in_desired_state = 0
        if response.data.nodes is not None:
            for node in response.data.nodes:
                if getattr(node, "lifecycle_state") == state_to_wait_for:
                    nodes_in_desired_state += 1
                    if nodes_in_desired_state == count_of_nodes_to_wait:
                        return True
        return False

    wait_response = oci.wait_until(
        client,
        get_fn(**{get_param: node_pool_id}),
        evaluate_response=check_nodes,
        max_wait_seconds=module.params.get("wait_timeout", MAX_WAIT_TIMEOUT_IN_SECONDS),
    )

    return wait_response.data


def create_and_wait(
    resource_type,
    create_fn,
    kwargs_create,
    client,
    get_fn,
    get_param,
    module,
    wait_applicable=True,
    states=None,
):
    result = dict(changed=False)
    try:
        response = oci_utils.call_with_backoff(create_fn, **kwargs_create)
        wr_id = response.headers.get("opc-work-request-id")
        get_wr_response = oci_utils.call_with_backoff(
            client.get_work_request, work_request_id=wr_id
        )
        result["work_request"] = to_dict(
            wait_on_work_request(client, get_wr_response, module)
        )
        _debug("Work request:{0}".format(result["work_request"]))
        result["changed"] = True
        if wait_applicable and module.params.get("wait", None):
            if states is None:
                states = [module.params.get("wait_until")] + DEFAULT_READY_STATES
            states = states + FAILED_STATES
            if resource_type == "cluster":
                resource_affected = result["work_request"]["resources"][0]
                _debug("Affected resources:{0}".format(resource_affected))
                resource = to_dict(
                    wait_on_resource(
                        client,
                        module,
                        get_fn,
                        {get_param: resource_affected["identifier"]},
                        states,
                    )
                )
                result[resource_type] = to_dict(resource)
                if result[resource_type]["lifecycle_state"] == "FAILED":
                    module.fail_json(
                        msg="Cluster reached FAILED state during creation."
                    )
            elif resource_type == "node_pool":
                for resource in result["work_request"]["resources"]:
                    if resource["entity_type"] == "nodepool":
                        node_pool_id = resource["identifier"]
                        break

                node_pool = wait_for_nodes(
                    module, client, get_fn, get_param, node_pool_id
                )
                result[resource_type] = to_dict(node_pool)
        return result

    except ServiceError as ex:
        module.fail_json(msg=ex.message)
