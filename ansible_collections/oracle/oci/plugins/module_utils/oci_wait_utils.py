# Copyright (c) 2019 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from . import oci_common_utils

try:
    import oci
    from oci.util import to_dict

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False

LIFECYCLE_STATE_WAITER_KEY = "LIFECYCLE_STATE_WAITER"
WORK_REQUEST_WAITER_KEY = "WORK_REQUEST_WAITER"
NONE_WAITER_KEY = "NONE_WAITER_KEY"


class Waiter:
    """Interface defining wait method"""

    def wait(self):
        raise NotImplementedError(
            "Expected to be implemented by the specific waiter classes."
        )


class BaseWaiter(Waiter):
    """Base class for various waiters"""

    def __init__(self, client, resource_helper, operation_response, wait_for_states):
        self.client = client
        self.operation_response = operation_response
        self.wait_for_states = wait_for_states
        self.resource_helper = resource_helper

    def get_fetch_func(self):
        raise NotImplementedError(
            "Expected to be implemented by the specific waiter classes."
        )

    def get_evaluate_response_lambda(self):
        raise NotImplementedError(
            "Expected to be implemented by the specific waiter classes."
        )

    def wait(self):
        if self.resource_helper.module.params.get("wait") is False:
            return self.operation_response.data

        fetch_func = self.get_fetch_func()
        initial_response = fetch_func()
        wait_response = oci.wait_until(
            self.client,
            initial_response,
            evaluate_response=self.get_evaluate_response_lambda(),
            max_wait_seconds=self.resource_helper.module.params.get(
                "wait_timeout", oci_common_utils.MAX_WAIT_TIMEOUT_IN_SECONDS
            ),
            fetch_func=fetch_func,
        )

        return self.get_resource_from_wait_response(wait_response)

    def get_resource_from_wait_response(self, wait_response):
        raise NotImplementedError(
            "Expected to be implemented by the specific waiter classes."
        )


class LifecycleStateWaiterBase(BaseWaiter):
    """Base class for various waiters"""

    def __init__(self, client, resource_helper, operation_response, wait_for_states):
        self.client = client
        self.operation_response = operation_response
        self.wait_for_states = wait_for_states
        self.resource_helper = resource_helper

    def get_fetch_func(self):
        return lambda **kwargs: self.resource_helper.get_resource()

    def get_evaluate_response_lambda(self):
        lowered_wait_for_states = [state.lower() for state in self.wait_for_states]
        return (
            lambda r: getattr(r.data, "lifecycle_state")
            and getattr(r.data, "lifecycle_state").lower() in lowered_wait_for_states
        )

    def get_resource_from_wait_response(self, wait_response):
        return wait_response.data


class LifecycleStateWaiter(LifecycleStateWaiterBase):
    """Waiter which waits on the lifecycle state of the resource"""

    def __init__(self, client, resource_helper, operation_response, wait_for_states):
        super(LifecycleStateWaiter, self).__init__(
            client, resource_helper, operation_response, wait_for_states
        )


class CreateOperationLifecycleStateWaiter(LifecycleStateWaiterBase):
    """Waiter which waits on the lifecycle state of the resource"""

    def __init__(self, client, resource_helper, operation_response, wait_for_states):
        super(CreateOperationLifecycleStateWaiter, self).__init__(
            client, resource_helper, operation_response, wait_for_states
        )

    def get_fetch_func(self):
        identifier = self.operation_response.data.id
        if not identifier:
            self.resource_helper.module.fail_json(
                "Error getting the resource identifier."
            )
        try:
            id_orig = self.resource_helper.module.params[
                self.resource_helper.get_module_resource_id_param()
            ]
        except NotImplementedError:
            return lambda **kwargs: self.resource_helper.get_resource()

        def fetch_func(**kwargs):
            self.resource_helper.module.params[
                self.resource_helper.get_module_resource_id_param()
            ] = identifier
            get_response = self.resource_helper.get_resource()
            self.resource_helper.module.params[
                self.resource_helper.get_module_resource_id_param()
            ] = id_orig
            return get_response

        return fetch_func


class CreateOperationWithCreateOnlyFieldsLifecycleStateWaiter(
    CreateOperationLifecycleStateWaiter
):
    """
    Waiter which waits on the lifecycle state of the resource, for resources where the
    CREATE operation returns important fields not returned by GET or LIST.

    Examples: CreateAuthToken, CreateCustomerSecretKey CreatePreauthendticatedRequest
    """

    def __init__(self, client, resource_helper, operation_response, wait_for_states):
        super(CreateOperationWithCreateOnlyFieldsLifecycleStateWaiter, self).__init__(
            client, resource_helper, operation_response, wait_for_states
        )

    def get_resource_from_wait_response(self, wait_response):
        # since the initial create response may not have returned an active state,
        # we override lifecycle_state here with the lifecycle_state when we finished waiting
        create_response = self.operation_response.data
        create_response.lifecycle_state = wait_response.data.lifecycle_state
        return create_response


class WorkRequestWaiter(BaseWaiter):
    """Waiter which waits on the work request"""

    def __init__(self, client, resource_helper, operation_response, wait_for_states):
        self.client = client
        self.resource_helper = resource_helper
        self.operation_response = operation_response
        self.wait_for_states = wait_for_states

    def get_fetch_func(self):
        return lambda **kwargs: self.client.get_work_request(
            self.operation_response.headers["opc-work-request-id"]
        )

    def get_evaluate_response_lambda(self):
        lowered_wait_for_states = [state.lower() for state in self.wait_for_states]
        return (
            lambda r: getattr(r.data, "status")
            and getattr(r.data, "status").lower() in lowered_wait_for_states
        )

    def get_resource_from_wait_response(self, wait_response):
        get_response = self.resource_helper.get_resource()
        return get_response.data


class CreateOperationWorkRequestWaiter(WorkRequestWaiter):
    """Waiter which waits on the work request"""

    def __init__(self, client, resource_helper, operation_response, wait_for_states):
        super(CreateOperationWorkRequestWaiter, self).__init__(
            client, resource_helper, operation_response, wait_for_states
        )

    def get_resource_from_wait_response(self, wait_response):
        entity_type = oci_common_utils.get_entity_type(
            self.resource_helper.resource_type
        )
        identifier = None
        for resource in wait_response.data.resources:
            if (
                hasattr(resource, "entity_type")
                and getattr(resource, "entity_type") == entity_type
            ):
                identifier = resource.identifier
        if not identifier:
            self.resource_helper.module.fail_json(
                msg="Could not get the resource identifier from work request response {0}".format(
                    to_dict(wait_response.data)
                )
            )
        get_response = self.resource_helper.get_get_fn()(identifier)
        return get_response.data


class NoneWaiter(Waiter):
    """Waiter which does not wait"""

    def __init__(self, client, resource_helper, operation_response, wait_for_states):
        self.client = client
        self.resource_helper = resource_helper
        self.operation_response = operation_response
        self.wait_for_states = wait_for_states

    def wait(self):
        return self.operation_response.data


class AuditConfigurationLifecycleStateWaiter(LifecycleStateWaiter):
    def __init__(self, client, resource_helper, operation_response, wait_for_states):
        super(AuditConfigurationLifecycleStateWaiter, self).__init__(
            client, resource_helper, operation_response, wait_for_states
        )

    def get_evaluate_response_lambda(self):
        # The update operation currently returns a work request id but the AuditClient currently does not support
        # waiting for the work request. So wait until the configuration is updated by checking the value.
        return (
            lambda r: r.data.retention_period_days
            == self.resource_helper.module.params.get("retention_period_days")
        )


class PeeringStatusWaiter(LifecycleStateWaiter):
    def __init__(self, client, resource_helper, operation_response, wait_for_states):
        super(PeeringStatusWaiter, self).__init__(
            client, resource_helper, operation_response, wait_for_states
        )

    def get_evaluate_response_lambda(self):
        # wait on peering_status instead of the default lifecycle_state
        return lambda r: r.data.peering_status == "PEERED"


# A map specifying the overrides for the default waiters.
# Key is a tuple consisting spec name, resource type and the operation and the value is the waiter class.
# For ex: ("waas", "waas_policy", oci_common_utils.UPDATE_OPERATION_KEY) -> CustomWaasWaiterClass
_WAITER_OVERRIDE_MAP = {
    # The audit update operation currently returns a work request id but the AuditClient currently does not support
    # waiting for the work request. So inject NoneWaiter and customize it to manually wait on the update condition.
    ("audit", "configuration", oci_common_utils.UPDATE_OPERATION_KEY): NoneWaiter,
    # # auth_token only returns 'token' field on create
    (
        "identity",
        "auth_token",
        oci_common_utils.CREATE_OPERATION_KEY,
    ): CreateOperationWithCreateOnlyFieldsLifecycleStateWaiter,
    # # customer_secret_key only returns 'key' field on create
    (
        "identity",
        "customer_secret_key",
        oci_common_utils.CREATE_OPERATION_KEY,
    ): CreateOperationWithCreateOnlyFieldsLifecycleStateWaiter,
    # TODO: currently waiter is only generated for DELETE operations with a single path parameter
    # so we need to manually override these
    (
        "identity",
        "customer_secret_key",
        oci_common_utils.DELETE_OPERATION_KEY,
    ): LifecycleStateWaiter,
    (
        "identity",
        "auth_token",
        oci_common_utils.DELETE_OPERATION_KEY,
    ): LifecycleStateWaiter,
    (
        "identity",
        "smtp_credential",
        oci_common_utils.DELETE_OPERATION_KEY,
    ): LifecycleStateWaiter,
    # update_tag can move a tag into ACTIVE or INACTIVE (based on is_retired flag) so we can't wait for active states
    # like usual or it will never complete when retiring a tag.
    # there is no other state we can reliably wait on to determine the update has completed and in all currently
    # known examples the UPDATE completes synchronously
    ("identity", "tag", oci_common_utils.UPDATE_OPERATION_KEY): NoneWaiter,
    # update_tag_namespace has the same issue as update_tag
    ("identity", "tag_namespace", oci_common_utils.UPDATE_OPERATION_KEY): NoneWaiter,
    # mfa_totp_device.seed is only returned on the "generate" call
    # so we need to disable waiting / polling such that we get
    # this field in the response
    (
        "identity",
        "mfa_totp_device",
        "{0}_{1}".format("GENERATE_TOTP_SEED", oci_common_utils.ACTION_OPERATION_KEY),
    ): NoneWaiter,
    # The lpg connect operation actually waits on peering_status unlike the NONE_WAITER_KEY generated by the module.
    # So override the waiter to wait on peering_status.
    (
        "core",
        "local_peering_gateway",
        "CONNECT_LOCAL_PEERING_GATEWAYS_ACTION",
    ): PeeringStatusWaiter,
    (
        "core",
        "remote_peering_connection",
        "CONNECT_REMOTE_PEERING_CONNECTIONS_ACTION",
    ): PeeringStatusWaiter,
}


def get_waiter_override(namespace, resource_type, operation):
    """Return the custom waiter class if any for the resource and operation. Else return None."""
    waiter_override_key = (namespace, resource_type, operation)
    if waiter_override_key in _WAITER_OVERRIDE_MAP:
        return _WAITER_OVERRIDE_MAP.get(waiter_override_key)
    # check if an override exists for ANY_OPERATION_KEY. This is helpful if we need a custom waiter for all(any)
    # resource operations
    waiter_override_key = (namespace, resource_type, oci_common_utils.ANY_OPERATION_KEY)
    if waiter_override_key in _WAITER_OVERRIDE_MAP:
        return _WAITER_OVERRIDE_MAP.get(waiter_override_key)
    return None


def get_waiter(
    waiter_type, operation, client, resource_helper, operation_response, wait_for_states
):
    """Return appropriate waiter object based on type and the operation."""
    # First check if there is any custom override for the waiter class. If exists, use it.
    waiter_override_class = get_waiter_override(
        resource_helper.namespace, resource_helper.resource_type, operation
    )
    if waiter_override_class:
        return waiter_override_class(
            client, resource_helper, operation_response, wait_for_states
        )
    if waiter_type == LIFECYCLE_STATE_WAITER_KEY:
        if operation == oci_common_utils.CREATE_OPERATION_KEY:
            return CreateOperationLifecycleStateWaiter(
                client, resource_helper, operation_response, wait_for_states
            )
        return LifecycleStateWaiter(
            client, resource_helper, operation_response, wait_for_states
        )
    elif waiter_type == WORK_REQUEST_WAITER_KEY:
        if operation == oci_common_utils.CREATE_OPERATION_KEY:
            return CreateOperationWorkRequestWaiter(
                client, resource_helper, operation_response, wait_for_states
            )
        return WorkRequestWaiter(
            client, resource_helper, operation_response, wait_for_states
        )
    return NoneWaiter(client, resource_helper, operation_response, wait_for_states)


def call_and_wait(
    call_fn,
    call_fn_args,
    call_fn_kwargs,
    waiter_type,
    operation,
    waiter_client,
    resource_helper,
    wait_for_states,
):
    """Call the given function and wait until the operation is completed and return the resource."""
    operation_response = oci_common_utils.call_with_backoff(
        call_fn, *call_fn_args, **call_fn_kwargs
    )
    waiter = get_waiter(
        waiter_type,
        operation,
        waiter_client,
        resource_helper,
        operation_response=operation_response,
        wait_for_states=wait_for_states,
    )
    return waiter.wait()
