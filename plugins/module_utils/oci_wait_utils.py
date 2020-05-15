# Copyright (c) 2019 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils

try:
    import oci
    from oci.util import to_dict
    from oci.exceptions import ServiceError

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False

LIFECYCLE_STATE_WAITER_KEY = "LIFECYCLE_STATE_WAITER"
WORK_REQUEST_WAITER_KEY = "WORK_REQUEST_WAITER"
NONE_WAITER_KEY = "NONE_WAITER_KEY"


logger = oci_common_utils.get_logger("oci_wait_utils")


def _debug(s):
    get_logger().debug(s)


def get_logger():
    return logger


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

    def verify_operation_succeeded(self, wait_response):
        # by default, if the wait ended it was successful
        # specific waiter classes may inspect additional information about
        # the wait_response to determine if it was a success
        # e.g. waiters can check if the terminal state is a success
        # state and not a failure state
        pass

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

        self.verify_operation_succeeded(wait_response)

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
        if hasattr(self.operation_response.data, "id"):
            identifier = self.operation_response.data.id
        else:
            identifier = getattr(
                self.operation_response.data,
                self.resource_helper.get_module_resource_id_param(),
            )
        if not identifier:
            self.resource_helper.module.fail_json(
                "Error getting the resource identifier."
            )
        try:
            if (self.resource_helper.get_module_resource_id_param() is not None) and (
                self.resource_helper.get_module_resource_id_param()
                in self.resource_helper.module.params
            ):
                id_orig = self.resource_helper.module.params[
                    self.resource_helper.get_module_resource_id_param()
                ]
            else:
                id_orig = None
        except NotImplementedError:
            return lambda **kwargs: self.resource_helper.get_resource()

        def fetch_func(**kwargs):
            self.resource_helper.module.params[
                self.resource_helper.get_module_resource_id_param()
            ] = identifier
            get_response = self.resource_helper.get_resource()
            if id_orig is not None:
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

    def _get_work_request_state_from_response(self, r):
        """
        Handles fetching work request state from any of multiple fields
        that different WorkRequest types define
        """
        if hasattr(r.data, "status") and getattr(r.data, "status"):
            state = getattr(r.data, "status")
        elif hasattr(r.data, "lifecycle_state") and getattr(r.data, "lifecycle_state"):
            state = getattr(r.data, "lifecycle_state")
        else:
            raise RuntimeError(
                "Unable to evaluate state of WorkRequest response. Did not contain status or lifecycle_state fields."
            )

        return state

    def _get_work_request_errors_from_failed_work_request(
        self, work_request_response, errors_attr=None
    ):
        if errors_attr:
            return getattr(work_request_response.data, errors_attr, None)
        if hasattr(work_request_response.data, "errors"):
            return work_request_response.data.errors
        if hasattr(work_request_response.data, "error_details"):
            return work_request_response.data.error_details
        if hasattr(self.client, "list_work_request_errors"):
            # almost all services have only 1 positional argument for list_work_request_errors
            # the exception is container_engine which also requires compartment ID, so try all
            # common / known signatures
            try:
                return self.client.list_work_request_errors(
                    work_request_response.data.id
                ).data
            except TypeError:
                try:
                    return self.client.list_work_request_errors(
                        work_request_response.data.compartment_id,
                        work_request_response.data.id,
                    ).data
                except TypeError:
                    pass
        return None

    def get_fetch_func(self):
        return lambda **kwargs: oci_common_utils.call_with_backoff(
            self.client.get_work_request,
            self.operation_response.headers["opc-work-request-id"],
        )

    def get_evaluate_response_lambda(self):
        lowered_wait_for_states = [state.lower() for state in self.wait_for_states]

        def evaluate_response(r):
            state = self._get_work_request_state_from_response(r)
            return state.lower() in lowered_wait_for_states

        return evaluate_response

    def verify_operation_succeeded(self, wait_response):
        state = self._get_work_request_state_from_response(wait_response)
        if state in oci_common_utils.WORK_REQUEST_FAILED_STATES:
            self.resource_helper.module.fail_json(
                msg="Work request {work_request_id} failed with errors: {errors}".format(
                    work_request_id=wait_response.data.id,
                    errors=self._get_work_request_errors_from_failed_work_request(
                        wait_response
                    ),
                )
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
        if hasattr(wait_response.data, "resources"):
            for resource in wait_response.data.resources:
                if (
                    hasattr(resource, "entity_type")
                    and getattr(resource, "entity_type") == entity_type
                ):
                    identifier = resource.identifier
        elif hasattr(
            wait_response.data, self.resource_helper.get_module_resource_id_param()
        ):
            # this handles LB style WorkRequests which contain a field "load_balancer_id"
            identifier = getattr(
                wait_response.data, self.resource_helper.get_module_resource_id_param()
            )

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


class PeeringStatusWaiter(LifecycleStateWaiter):
    def __init__(self, client, resource_helper, operation_response, wait_for_states):
        super(PeeringStatusWaiter, self).__init__(
            client, resource_helper, operation_response, wait_for_states
        )

    def get_evaluate_response_lambda(self):
        # wait on peering_status instead of the default lifecycle_state
        return lambda r: r.data.peering_status == "PEERED"


class CreateCompartmentOperationLifecycleStateWaiter(
    CreateOperationLifecycleStateWaiter
):
    """Waiter which waits on the lifecycle state of the resource"""

    def __init__(self, client, resource_helper, operation_response, wait_for_states):
        super(CreateCompartmentOperationLifecycleStateWaiter, self).__init__(
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

            try:
                get_response = self.resource_helper.get_resource()
            except ServiceError as se:
                # create compartment has a service issue where CREATE
                # returns with lifecycle_state = ACTIVE before the
                # compartment is available to be fetched via a GET request
                # This is because it takes few seconds for the permissions on a
                # compartment to be ready.
                # Wait for few seconds before attempting a get call on compartment.
                if se.status != 404:
                    raise

                # return a dummy response to allow waiting to continue
                get_response = oci_common_utils.get_default_response_from_resource(
                    oci.identity.models.Compartment()
                )

            self.resource_helper.module.params[
                self.resource_helper.get_module_resource_id_param()
            ] = id_orig
            return get_response

        return fetch_func


class VolumeCreateWaitUntilCopyIsDoneWaiter(CreateOperationLifecycleStateWaiter):
    def get_evaluate_response_lambda(self):
        return lambda r: not hasattr(r.data, "is_hydrated") or getattr(
            r.data, "is_hydrated"
        )


class CopyObjectWorkRequestWaiter(WorkRequestWaiter):
    def get_resource_from_wait_response(self, wait_response):
        return wait_response.data


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
    ("core", "local_peering_gateway", "CONNECT_ACTION",): PeeringStatusWaiter,
    ("core", "remote_peering_connection", "CONNECT_ACTION",): PeeringStatusWaiter,
    # create compartment has a service issue where it returns before resource can be fetched with a GET
    # thus we need a custom waiter that continues to fetch even if the first few fetches return a 404
    (
        "identity",
        "compartment",
        oci_common_utils.CREATE_OPERATION_KEY,
    ): CreateCompartmentOperationLifecycleStateWaiter,
    # The generated copy method in boot_volume_backup_actions waits on the source backup lifecycle state. But the source
    # backup remains in AVAILABLE state when the copy is in progress. So override to not wait here and add a
    # customisation to wait until the copy is done.
    (
        "core",
        "boot_volume_backup",
        "{0}_{1}".format("COPY", oci_common_utils.ACTION_OPERATION_KEY,),
    ): NoneWaiter,
    # The generated copy method in volume_backup_actions waits on the source backup lifecycle state. But the source
    # backup remains in AVAILABLE state when the copy is in progress. So override to not wait here and add a
    # customisation to wait until the copy is done.
    (
        "core",
        "volume_backup",
        "{0}_{1}".format("COPY", oci_common_utils.ACTION_OPERATION_KEY,),
    ): NoneWaiter,
    (
        "core",
        "boot_volume",
        oci_common_utils.CREATE_OPERATION_KEY,
    ): VolumeCreateWaitUntilCopyIsDoneWaiter,
    (
        "core",
        "volume",
        oci_common_utils.CREATE_OPERATION_KEY,
    ): VolumeCreateWaitUntilCopyIsDoneWaiter,
    # the load balancer work requests don't contain the OCID of the resource being created
    # so we want to fallback to the default WorkRequestWaiter which calls the generated
    # get_resource() method to retrieve the resource
    (
        "load_balancer",
        "backend_set",
        oci_common_utils.CREATE_OPERATION_KEY,
    ): WorkRequestWaiter,
    (
        "load_balancer",
        "backend",
        oci_common_utils.CREATE_OPERATION_KEY,
    ): WorkRequestWaiter,
    (
        "load_balancer",
        "certificate",
        oci_common_utils.CREATE_OPERATION_KEY,
    ): WorkRequestWaiter,
    (
        "load_balancer",
        "hostname",
        oci_common_utils.CREATE_OPERATION_KEY,
    ): WorkRequestWaiter,
    (
        "load_balancer",
        "listener",
        oci_common_utils.CREATE_OPERATION_KEY,
    ): WorkRequestWaiter,
    (
        "load_balancer",
        "path_route_set",
        oci_common_utils.CREATE_OPERATION_KEY,
    ): WorkRequestWaiter,
    (
        "load_balancer",
        "rule_set",
        oci_common_utils.CREATE_OPERATION_KEY,
    ): WorkRequestWaiter,
    (
        "object_storage",
        "object",
        "{0}_{1}".format("COPY", oci_common_utils.ACTION_OPERATION_KEY,),
    ): CopyObjectWorkRequestWaiter,
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
