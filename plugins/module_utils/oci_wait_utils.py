# Copyright (c) 2019, 2021 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function
import time

__metaclass__ = type

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_config_utils,
)

try:
    import oci
    from oci.util import to_dict
    from oci.exceptions import ServiceError
    from oci.core import ComputeClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False

WORK_REQUEST_HEADER = "opc-work-request-id"

LIFECYCLE_STATE_WAITER_KEY = "LIFECYCLE_STATE_WAITER"
WORK_REQUEST_WAITER_KEY = "WORK_REQUEST_WAITER"
NONE_WAITER_KEY = "NONE_WAITER_KEY"

# Services where if no opc-work-request-id is returned we will fallback to waiting
# via lifecycle state
# This is something that ideally services should fix, but we want our modules to continue
# working before that happens
# If we can reliably determine that no opc-work-request returned indicates immediate completion
# and no waiting is necessary then we can build that case into WorkRequestWaiter
SERVICES_WHERE_WORK_REQUEST_WAITING_SHOULD_FALLBACK_TO_LIFECYCLE_WAITING = [
    "database",
    "mysql",
    "resource_manager",
    "core",
]

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
            max_wait_seconds=self.resource_helper.get_wait_timeout(),
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

    def verify_operation_succeeded(self, wait_response):
        if wait_response.data and hasattr(wait_response.data, "lifecycle_state"):
            if (
                wait_response.data.lifecycle_state
                in self.resource_helper.get_resource_failed_states()
            ):
                self.resource_helper.module.fail_json(
                    msg="Operation failed as resource entered into a failure state: {failure_state}".format(
                        failure_state=wait_response.data.lifecycle_state
                    )
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

    def get_identifier_from_resource(self, resource):
        if hasattr(resource, "id"):
            identifier = resource.id
        else:
            identifier = getattr(
                resource, self.resource_helper.get_module_resource_id_param(),
            )
        return identifier

    def get_fetch_func(self):
        identifier = self.get_identifier_from_resource(self.operation_response.data)
        if not identifier:
            self.resource_helper.module.fail_json(
                msg="Error getting the resource identifier."
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


class CreateDataCatalogWaiter(CreateOperationLifecycleStateWaiter):
    """Waiter which waits on the lifecycle state of the resource"""

    def __init__(self, client, resource_helper, operation_response, wait_for_states):
        super(CreateDataCatalogWaiter, self).__init__(
            client, resource_helper, operation_response, wait_for_states
        )

    def get_identifier_from_resource(self, resource):
        return resource.key


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
            self.operation_response.headers[WORK_REQUEST_HEADER],
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
        entity_type = self.resource_helper.get_entity_type()
        identifier = None
        if hasattr(wait_response.data, "resources"):
            identifier = get_resource_identifier_from_wait_response(
                wait_response.data, entity_type
            )
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


class CreateDatabaseOperationWorkRequestWaiter(CreateOperationWorkRequestWaiter):
    def __init__(self, client, resource_helper, operation_response, wait_for_states):
        super(CreateDatabaseOperationWorkRequestWaiter, self).__init__(
            client, resource_helper, operation_response, wait_for_states
        )

    def get_resource_from_wait_response(self, wait_response):
        entity_type = self.resource_helper.get_entity_type()
        identifier = None
        # work-request response for operation - create clone database returns two resources -
        # source db & cloned db. To return cloned db additional check on `action_type` is
        # required.
        for resource in wait_response.data.resources:
            if (
                hasattr(resource, "entity_type")
                and getattr(resource, "entity_type").lower().strip().replace("-", "")
                == entity_type.lower()
                and getattr(resource, "action_type") == "CREATED"
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
                msg="Error getting the resource identifier."
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


class ChangeLogGroupWorkRequestWaiter(WorkRequestWaiter):
    # Once the operation - `change_log_log_group` is successful log_group_id of log changes to `target_log_group_id`
    # Operation returns response without body thus in order to retrieve `Log` resource we have to pass
    # `target_log_group_id` instead of `log_group_id`.
    def get_resource_from_wait_response(self, wait_response):
        sleep_interval_seconds = 1
        start_time = time.time()
        max_wait_seconds = self.resource_helper.get_wait_timeout()

        # GET call throws NotFoundException if the request is made immediately after changing log group of specified log
        # We avoid giving back NotFoundException to user by making repetitive calls until max wait time is exceeded.
        while (
            self.is_resource_not_found()
            and time.time() - start_time <= max_wait_seconds
        ):
            time.sleep(sleep_interval_seconds)
            sleep_interval_seconds = min(sleep_interval_seconds * 2, max_wait_seconds)

        # return None when Maximum wait time has been exceeded.
        if time.time() - start_time > max_wait_seconds:
            return None

        return oci_common_utils.call_with_backoff(
            self.resource_helper.client.get_log,
            log_group_id=self.resource_helper.module.params.get("target_log_group_id"),
            log_id=self.resource_helper.module.params.get("log_id"),
        ).data

    def is_resource_not_found(self):
        try:
            oci_common_utils.call_with_backoff(
                self.resource_helper.client.get_log,
                log_group_id=self.resource_helper.module.params.get(
                    "target_log_group_id"
                ),
                log_id=self.resource_helper.module.params.get("log_id"),
            )
        except ServiceError as se:
            if se.status == 404:
                return True
            else:
                raise
        return False


class InstanceConfigurationLaunchInstanceWorkRequestWaiter(WorkRequestWaiter):
    # launch action creates an instance. So it makes more sense to return the created instance but the default
    # implementation returns the instance_configuration. So override to return the created instance instead.
    def get_resource_from_wait_response(self, wait_response):
        if not (
            hasattr(wait_response.data, "resources") and wait_response.data.resources
        ):
            self.resource_helper.module.fail_json(
                msg="Could not get instance id from work request response {data}".format(
                    data=wait_response.data
                )
            )
        instance_id = None
        for resource in wait_response.data.resources:
            if resource.entity_type.lower() == "instance":
                instance_id = resource.identifier
        if not instance_id:
            self.resource_helper.module.fail_json(
                msg="Could not get instance id from work request response {data}".format(
                    data=wait_response.data
                )
            )
        compute_client = oci_config_utils.create_service_client(
            self.resource_helper.module, ComputeClient
        )
        return compute_client.get_instance(instance_id=instance_id).data


class NamespaceActionWorkRequestWaiter(WorkRequestWaiter):
    def get_fetch_func(self):
        return lambda **kwargs: oci_common_utils.call_with_backoff(
            self.client.get_work_request,
            work_request_id=self.operation_response.headers[WORK_REQUEST_HEADER],
            namespace_name=self.resource_helper.module.params.get("namespace_name"),
        )


class BulkEditTagOperationWorkRequestWaiter(WorkRequestWaiter):
    def get_fetch_func(self):
        return lambda **kwargs: oci_common_utils.call_with_backoff(
            self.client.get_tagging_work_request,
            work_request_id=self.operation_response.headers[WORK_REQUEST_HEADER],
        )

    # returned response has no body content.
    def get_resource_from_wait_response(self, wait_response):
        return None


class UpdateAutonomousDatabaseWorkRequestWaiter(WorkRequestWaiter):
    def __init__(self, client, resource_helper, operation_response, wait_for_states):
        super(UpdateAutonomousDatabaseWorkRequestWaiter, self).__init__(
            client, resource_helper, operation_response, wait_for_states
        )

    def wait(self):
        if self.resource_helper.module.params.get("wait") is False:
            return self.operation_response.data

        fetch_funcs = self.get_fetch_funcs()
        for fetch_func in fetch_funcs:
            initial_response = fetch_func()
            wait_response = oci.wait_until(
                self.client,
                initial_response,
                evaluate_response=self.get_evaluate_response_lambda(),
                max_wait_seconds=self.resource_helper.get_wait_timeout(),
                fetch_func=fetch_func,
            )

            self.verify_operation_succeeded(wait_response)

        get_response = self.resource_helper.get_resource()
        return get_response.data

    def get_fetch_funcs(self):
        opc_work_request_ids = self.operation_response.headers[
            WORK_REQUEST_HEADER
        ].split(",")

        return [
            lambda work_request_id=opc_work_request_id, **kwargs: oci_common_utils.call_with_backoff(
                self.client.get_work_request, work_request_id,
            )
            for opc_work_request_id in opc_work_request_ids
        ]


class NosqlChangeCompartmentCustomWaiter(WorkRequestWaiter):
    # Getting the resource immediately after the work request succeeds gives a 404 error.
    def get_resource_from_wait_response(self, wait_response):
        time.sleep(30)
        get_response = self.resource_helper.get_resource()
        return get_response.data


# getting the resource requires identifier of sdk resource
# but api returns identifier for parent resource i.e paigateway
# using get_matching_resource to get the resource after creation
class ApiGatewayCreateSdkWorkRequestWaiter(CreateOperationWorkRequestWaiter):
    def __init__(self, client, resource_helper, operation_response, wait_for_states):
        super(ApiGatewayCreateSdkWorkRequestWaiter, self).__init__(
            client, resource_helper, operation_response, wait_for_states
        )

    # We get identifier for apigateway resource and not sdk resource
    # return get_matching resource in that case
    # we fail the task if we couldnt find the resource post creation (rare case)
    def get_resource_from_wait_response(self, wait_response):
        matching_resource = self.resource_helper.get_matching_resource()
        if matching_resource is None:
            self.resource_helper.module.fail_json(
                msg="Resource created successfuly. Error while fetching the resource"
            )
        return matching_resource


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
    (
        "identity",
        "smtp_credential",
        oci_common_utils.CREATE_OPERATION_KEY,
    ): CreateOperationWithCreateOnlyFieldsLifecycleStateWaiter,
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
        "routing_policy",
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
        "load_balancer",
        "ssl_cipher_suite",
        oci_common_utils.CREATE_OPERATION_KEY,
    ): WorkRequestWaiter,
    (
        "object_storage",
        "object",
        "{0}_{1}".format("COPY", oci_common_utils.ACTION_OPERATION_KEY,),
    ): CopyObjectWorkRequestWaiter,
    (
        "vault",
        "secret",
        "{0}_{1}".format(
            "CANCEL_SECRET_DELETION", oci_common_utils.ACTION_OPERATION_KEY
        ),
    ): LifecycleStateWaiter,
    (
        "vault",
        "secret",
        "{0}_{1}".format(
            "SCHEDULE_SECRET_DELETION", oci_common_utils.ACTION_OPERATION_KEY
        ),
    ): LifecycleStateWaiter,
    (
        "core",
        "instance_configuration",
        "{0}_{1}".format("LAUNCH", oci_common_utils.ACTION_OPERATION_KEY,),
    ): InstanceConfigurationLaunchInstanceWorkRequestWaiter,
    ("nosql", "index", oci_common_utils.CREATE_OPERATION_KEY,): WorkRequestWaiter,
    (
        "data_catalog",
        "data_asset",
        oci_common_utils.CREATE_OPERATION_KEY,
    ): CreateDataCatalogWaiter,
    (
        "data_catalog",
        "connection",
        oci_common_utils.CREATE_OPERATION_KEY,
    ): CreateDataCatalogWaiter,
    (
        "data_catalog",
        "namespace",
        oci_common_utils.CREATE_OPERATION_KEY,
    ): CreateDataCatalogWaiter,
    (
        "data_catalog",
        "custom_property",
        oci_common_utils.CREATE_OPERATION_KEY,
    ): CreateDataCatalogWaiter,
    # mysql UpdateDbSystem doesn't return anything and by default doesn't have a waiter
    # we need to override this to use a lifecycle waiter since mysql DbSystem model does
    # have a lifecycle state field
    ("mysql", "backup", oci_common_utils.UPDATE_OPERATION_KEY,): LifecycleStateWaiter,
    # identity_tag's bulk_delete action does not return anything by default. Hence, cannot
    # wait for any lifecycle state change
    (
        "identity",
        "tag",
        "{0}_{1}".format("BULK_DELETE", oci_common_utils.ACTION_OPERATION_KEY,),
    ): NoneWaiter,
    # identity_tag_namespace's cascade_delete action does not return anything by default.
    # Hence, cannot wait for any lifecycle state change
    (
        "identity",
        "tag_namespace",
        "{0}_{1}".format("CASCADE_DELETE", oci_common_utils.ACTION_OPERATION_KEY,),
    ): NoneWaiter,
    # identity_compartment's bulk_move_resources action does not return anything by default.
    # Hence, cannot wait for any lifecycle state change
    (
        "identity",
        "compartment",
        "{0}_{1}".format("BULK_MOVE_RESOURCES", oci_common_utils.ACTION_OPERATION_KEY,),
    ): NoneWaiter,
    # identity_compartment's bulk_delete_resources action does not return anything by default.
    # Hence, cannot wait for any lifecycle state change
    (
        "identity",
        "compartment",
        "{0}_{1}".format(
            "BULK_DELETE_RESOURCES", oci_common_utils.ACTION_OPERATION_KEY,
        ),
    ): NoneWaiter,
    (
        "logging",
        "log",
        "{0}_{1}".format(
            "CHANGE_LOG_LOG_GROUP", oci_common_utils.ACTION_OPERATION_KEY,
        ),
    ): ChangeLogGroupWorkRequestWaiter,
    (
        "log_analytics",
        "namespace",
        "{0}_{1}".format("ONBOARD", oci_common_utils.ACTION_OPERATION_KEY,),
    ): NamespaceActionWorkRequestWaiter,
    (
        "log_analytics",
        "namespace",
        "{0}_{1}".format("OFFBOARD", oci_common_utils.ACTION_OPERATION_KEY,),
    ): NamespaceActionWorkRequestWaiter,
    (
        "database",
        "autonomous_database",
        oci_common_utils.CREATE_OPERATION_KEY,
    ): CreateDatabaseOperationWorkRequestWaiter,
    # As External Databases need a connector to reach to the 'Available' state which is not done as part of the DB generation,
    # hence marking as NoWaiter so that "Not Connected" state can be considered
    (
        "database",
        "external_pluggable_database",
        oci_common_utils.CREATE_OPERATION_KEY,
    ): NoneWaiter,
    (
        "database",
        "external_non_container_database",
        oci_common_utils.CREATE_OPERATION_KEY,
    ): NoneWaiter,
    (
        "database",
        "external_container_database",
        oci_common_utils.CREATE_OPERATION_KEY,
    ): NoneWaiter,
    # For Marketplace Publications, resource creation and
    # resource updation takes way too long and involves manual
    # approval from the service team that can take a lot of time.
    ("marketplace", "publication", oci_common_utils.CREATE_OPERATION_KEY,): NoneWaiter,
    ("marketplace", "publication", oci_common_utils.UPDATE_OPERATION_KEY,): NoneWaiter,
    # work-request generated for operation `bulk_edit` can not be fetched using the generic Identity work-request api.
    # all tagging operations, use tagging work request api.
    (
        "identity",
        "tag",
        "{0}_{1}".format("BULK_EDIT", oci_common_utils.ACTION_OPERATION_KEY,),
    ): BulkEditTagOperationWorkRequestWaiter,
    (
        "database",
        "autonomous_database",
        oci_common_utils.UPDATE_OPERATION_KEY,
    ): UpdateAutonomousDatabaseWorkRequestWaiter,
    (
        "core",
        "instance_pool_instance",
        oci_common_utils.CREATE_OPERATION_KEY,
    ): WorkRequestWaiter,
    (
        "nosql",
        "table",
        "{0}_{1}".format("CHANGE_COMPARTMENT", oci_common_utils.ACTION_OPERATION_KEY,),
    ): NosqlChangeCompartmentCustomWaiter,
    # the backend_set,backend,listener work requests doesn't contain the OCID of the resource being created
    # so we want to fallback to the default WorkRequestWaiter which calls the generated
    # get_resource() method to retrieve the resource
    (
        "network_load_balancer",
        "backend_set",
        oci_common_utils.CREATE_OPERATION_KEY,
    ): WorkRequestWaiter,
    (
        "network_load_balancer",
        "backend",
        oci_common_utils.CREATE_OPERATION_KEY,
    ): WorkRequestWaiter,
    (
        "network_load_balancer",
        "listener",
        oci_common_utils.CREATE_OPERATION_KEY,
    ): WorkRequestWaiter,
    (
        "analytics",
        "vanity_url",
        oci_common_utils.CREATE_OPERATION_KEY,
    ): WorkRequestWaiter,
    (
        "analytics",
        "private_access_channel",
        oci_common_utils.CREATE_OPERATION_KEY,
    ): WorkRequestWaiter,
    (
        "apigateway",
        "sdk",
        oci_common_utils.CREATE_OPERATION_KEY,
    ): ApiGatewayCreateSdkWorkRequestWaiter,
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
        resource_helper.namespace, resource_helper.resource_type, operation,
    )
    if waiter_override_class:
        return waiter_override_class(
            client, resource_helper, operation_response, wait_for_states
        )

    if (
        resource_helper.namespace
        in SERVICES_WHERE_WORK_REQUEST_WAITING_SHOULD_FALLBACK_TO_LIFECYCLE_WAITING
        and waiter_type == WORK_REQUEST_WAITER_KEY
        and operation_response
        and operation_response.headers
        and WORK_REQUEST_HEADER not in operation_response.headers
    ):
        # this is a work request operation but no opc-work-request-id was returned
        # some services (e.g. dbaas) have this known implementation issue so we allow
        # falling back to lifecycle based waiting
        _debug(
            "Operation {resource_type} {operation} did not return work request id. Falling back to lifecycle state based waiting".format(
                operation=operation, resource_type=resource_helper.resource_type
            )
        )
        waiter_type = LIFECYCLE_STATE_WAITER_KEY
        if resource_helper.module.params.get(
            "action"
        ) and operation == "{0}_{1}".format(
            resource_helper.module.params.get("action").upper(),
            oci_common_utils.ACTION_OPERATION_KEY,
        ):
            wait_for_states = resource_helper.get_action_desired_states(
                resource_helper.module.params.get("action")
            )
        elif operation == oci_common_utils.DELETE_OPERATION_KEY:
            wait_for_states = resource_helper.get_resource_terminated_states()
        elif (
            operation == oci_common_utils.CREATE_OPERATION_KEY
            or operation == oci_common_utils.UPDATE_OPERATION_KEY
        ):
            wait_for_states = resource_helper.get_resource_active_states()
        else:
            resource_helper.module.fail_json(
                msg="Unable to wait on operation, work request ID was not returned and operation type is unrecognized: {operation_key}".format(
                    operation_key=operation
                )
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


def get_wait_for_states_with_failed_states(wait_for_states, resource_helper):
    try:
        resource_failure_states = resource_helper.get_resource_failed_states()
        if resource_failure_states:
            wait_for_states = list(set(wait_for_states + resource_failure_states))
    except NotImplementedError:
        pass
    return wait_for_states


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
    # Add the failure states so that when an operation fails and the resource goes into failed state we fail and don't
    # wait until the timeout. This seems to be a good place to put this instead of duplicating it in multiple places.
    if waiter_type == LIFECYCLE_STATE_WAITER_KEY:
        wait_for_states = get_wait_for_states_with_failed_states(
            wait_for_states, resource_helper
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


def get_resource_identifier_from_wait_response(wait_response, entity_type):
    identifier = None
    for resource in wait_response.resources:
        if (
            hasattr(resource, "entity_type")
            and getattr(resource, "entity_type").lower().strip().replace("-", "")
            == entity_type.lower()
        ):
            identifier = resource.identifier
        # this handles Analytics Instance & Digital Assistant Instance style WorkRequests which contains a field
        # 'resource_type' instead of 'entity_type'
        elif (
            hasattr(resource, "resource_type")
            and getattr(resource, "resource_type").lower().strip().replace("_", "")
            == entity_type.lower()
        ):
            if hasattr(resource, "identifier"):
                identifier = resource.identifier
            # identifier that was assigned when ODA instance was created.
            elif hasattr(resource, "resource_id"):
                identifier = resource.resource_id
    return identifier
