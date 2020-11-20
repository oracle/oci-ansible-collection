# Copyright (c) 2020 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)

try:
    from oci.util import to_dict

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False

logger = oci_common_utils.get_logger("oci_dns_custom_helpers")


def _debug(s):
    get_logger().debug(s)


def get_logger():
    return logger


class ZoneHelperCustom:
    def get_create_model_dict_for_idempotence_check(self, create_model):
        create_model_dict = super(
            ZoneHelperCustom, self
        ).get_create_model_dict_for_idempotence_check(create_model)
        # migration_source is a discriminator field and dynect_migration_details is not available in the get model
        create_model_dict.pop("migration_source", None)
        create_model_dict.pop("dynect_migration_details", None)
        return create_model_dict

    def get_resource(self):
        if self.module.params.get("scope") is not None:
            return oci_common_utils.call_with_backoff(
                self.client.get_zone,
                zone_name_or_id=self.module.params.get("zone_name_or_id"),
                scope=self.module.params.get("scope"),
                view_id=self.module.params.get("view_id"),
            )
        return oci_common_utils.call_with_backoff(
            self.client.get_zone,
            zone_name_or_id=self.module.params.get("zone_name_or_id"),
            view_id=self.module.params.get("view_id"),
        )

    def get_get_model_from_summary_model(self, summary_model):
        if self.module.params.get("scope") is not None:
            return oci_common_utils.call_with_backoff(
                self.client.get_zone,
                zone_name_or_id=summary_model.id,
                scope=self.module.params.get("scope"),
            ).data
        return super(ZoneHelperCustom, self).get_get_model_from_summary_model(
            summary_model
        )

    # scope is an enum parameter with allowed values ["GLOBAL", "PRIVATE"]
    # Python sdk validates the enum parameters to check if it is in the list of allowed values even when it is None.
    # API throws an error when scope is set to GLOBAL. API expects this parameter not to be passed when the scope is
    # GLOBAL but we cannot do that because of the python sdk validation.
    def create_resource(self):
        create_details = self.get_create_model()
        call_fn_kwargs = dict(
            create_zone_details=create_details,
            compartment_id=self.module.params.get("compartment_id"),
            view_id=self.module.params.get("view_id"),
        )
        if self.module.params.get("scope") is not None:
            call_fn_kwargs["scope"] = self.module.params["scope"]
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_zone,
            call_fn_args=(),
            call_fn_kwargs=call_fn_kwargs,
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def update_resource(self):
        update_details = self.get_update_model()
        call_fn_kwargs = dict(
            zone_name_or_id=self.module.params.get("zone_name_or_id"),
            update_zone_details=update_details,
            if_unmodified_since=self.module.params.get("if_unmodified_since"),
            view_id=self.module.params.get("view_id"),
            compartment_id=self.module.params.get("compartment_id"),
        )
        if self.module.params.get("scope") is not None:
            call_fn_kwargs["scope"] = self.module.params["scope"]
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_zone,
            call_fn_args=(),
            call_fn_kwargs=call_fn_kwargs,
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        call_fn_kwargs = dict(
            zone_name_or_id=self.module.params.get("zone_name_or_id"),
            if_unmodified_since=self.module.params.get("if_unmodified_since"),
            view_id=self.module.params.get("view_id"),
            compartment_id=self.module.params.get("compartment_id"),
        )
        if self.module.params.get("scope") is not None:
            call_fn_kwargs["scope"] = self.module.params["scope"]
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_zone,
            call_fn_args=(),
            call_fn_kwargs=call_fn_kwargs,
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


# This class handles some of the common customisations across some of the dns modules which works on a collection of
# records. For ex: zone_records, domain_records, rrset etc.
#
# Some of the common customisations that apply to these modules are:
#   * Have both update and patch methods and differentiators method customisations (is_update, is_patch). There is no
#     clear differentiation between between update and patch in general since they both need a resource id and same
#     state value. But in the DNS records modules, we can differentiate them using the existence of some attributes like
#     update_items, patch_items etc.
#   * update_items and patch_items are mutually exclusive
#   * update and patch methods do not support check mode and check changed based on the changed resource value
#     after performing the operation. This is done so that some of the fields (for ex: rdata) is normalized in the
#     server and would not be same to what are sent during create. We need third party libraries if we need to normalize
#     and perform the check which is not an option since this would put a dependency on that for using our modules.
#     Another option would be to just exclude those attributes but I don't think it is a good idea either since we
#     would not be able to handle updates in those fields. This behaviour is consistent with the legacy modules.
class DNSRecordsHelperCustom:
    def __init__(self, *args, **kwargs):
        super(DNSRecordsHelperCustom, self).__init__(*args, **kwargs)
        if (
            self.module.params.get("update_items") is not None
            and self.module.params.get("patch_items") is not None
        ):
            self.module.fail_json(
                msg="update_items and patch_items are mutually exclusive"
            )
        self.module.params["items"] = self.module.params.get(
            "update_items"
        ) or self.module.params.get("patch_items")

    def is_update(self):
        is_update = super(DNSRecordsHelperCustom, self).is_update()
        if not is_update:
            return False
        if self.module.params.get("update_items") is None:
            return False
        return True

    def is_patch(self):
        is_patch = super(DNSRecordsHelperCustom, self).is_patch()
        if not is_patch:
            return False
        if self.module.params.get("patch_items") is None:
            return False
        return True

    def update(self):
        existing_zone_records = self.get_resource().data
        updated_resource = self.update_resource()
        updated_zone_records = self.get_resource().data
        changed = not oci_common_utils.compare_lists(
            to_dict(updated_zone_records), to_dict(existing_zone_records)
        )
        return self.prepare_result(
            changed=changed,
            resource_type=self.resource_type,
            resource=to_dict(updated_resource.items),
        )

    def patch(self):
        existing_zone_records = self.get_resource().data
        patched_resource = self.patch_resource()
        patched_zone_records = self.get_resource().data
        changed = not oci_common_utils.compare_lists(
            to_dict(patched_zone_records), to_dict(existing_zone_records)
        )
        return self.prepare_result(
            changed=changed,
            resource_type=self.resource_type,
            resource=to_dict(patched_resource.items),
        )


class ZoneRecordsHelperCustom(DNSRecordsHelperCustom):
    def get_resource(self):
        if self.module.params.get("scope") is not None:
            return oci_common_utils.get_default_response_from_resource(
                oci_common_utils.list_all_resources(
                    self.client.get_zone_records,
                    zone_name_or_id=self.module.params.get("zone_name_or_id"),
                    scope=self.module.params.get("scope"),
                    view_id=self.module.params.get("view_id"),
                ).items
            )
        return oci_common_utils.get_default_response_from_resource(
            oci_common_utils.list_all_resources(
                self.client.get_zone_records,
                zone_name_or_id=self.module.params.get("zone_name_or_id"),
                view_id=self.module.params.get("view_id"),
            ).items
        )

    def update_resource(self):
        update_details = self.get_update_model()
        call_fn_kwargs = dict(
            zone_name_or_id=self.module.params.get("zone_name_or_id"),
            update_zone_records_details=update_details,
            if_unmodified_since=self.module.params.get("if_unmodified_since"),
            view_id=self.module.params.get("view_id"),
            compartment_id=self.module.params.get("compartment_id"),
        )
        if self.module.params.get("scope") is not None:
            call_fn_kwargs["scope"] = self.module.params["scope"]
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_zone_records,
            call_fn_args=(),
            call_fn_kwargs=call_fn_kwargs,
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def patch_resource(self):
        patch_details = self.get_patch_model()
        call_fn_kwargs = dict(
            zone_name_or_id=self.module.params.get("zone_name_or_id"),
            patch_zone_records_details=patch_details,
            if_unmodified_since=self.module.params.get("if_unmodified_since"),
            view_id=self.module.params.get("view_id"),
            compartment_id=self.module.params.get("compartment_id"),
        )
        if self.module.params.get("scope") is not None:
            call_fn_kwargs["scope"] = self.module.params["scope"]
        # self.module.fail_json(msg=to_dict(call_fn_kwargs))
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.patch_zone_records,
            call_fn_args=(),
            call_fn_kwargs=call_fn_kwargs,
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.PATCH_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.PATCH_OPERATION_KEY,
            ),
        )


class DomainRecordsHelperCustom(DNSRecordsHelperCustom):
    def get_resource(self):
        if self.module.params.get("scope") is not None:
            return oci_common_utils.get_default_response_from_resource(
                oci_common_utils.list_all_resources(
                    self.client.get_domain_records,
                    zone_name_or_id=self.module.params.get("zone_name_or_id"),
                    domain=self.module.params.get("domain"),
                    scope=self.module.params.get("scope"),
                    view_id=self.module.params.get("view_id"),
                ).items
            )
        return oci_common_utils.get_default_response_from_resource(
            oci_common_utils.list_all_resources(
                self.client.get_domain_records,
                zone_name_or_id=self.module.params.get("zone_name_or_id"),
                domain=self.module.params.get("domain"),
                view_id=self.module.params.get("view_id"),
            ).items
        )

    def update_resource(self):
        update_details = self.get_update_model()
        call_fn_kwargs = dict(
            zone_name_or_id=self.module.params.get("zone_name_or_id"),
            domain=self.module.params.get("domain"),
            update_domain_records_details=update_details,
            if_unmodified_since=self.module.params.get("if_unmodified_since"),
            view_id=self.module.params.get("view_id"),
            compartment_id=self.module.params.get("compartment_id"),
        )
        if self.module.params.get("scope") is not None:
            call_fn_kwargs["scope"] = self.module.params["scope"]
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_domain_records,
            call_fn_args=(),
            call_fn_kwargs=call_fn_kwargs,
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def patch_resource(self):
        patch_details = self.get_patch_model()
        call_fn_kwargs = dict(
            zone_name_or_id=self.module.params.get("zone_name_or_id"),
            domain=self.module.params.get("domain"),
            patch_domain_records_details=patch_details,
            if_unmodified_since=self.module.params.get("if_unmodified_since"),
            view_id=self.module.params.get("view_id"),
            compartment_id=self.module.params.get("compartment_id"),
        )
        if self.module.params.get("scope") is not None:
            call_fn_kwargs["scope"] = self.module.params["scope"]
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.patch_domain_records,
            call_fn_args=(),
            call_fn_kwargs=call_fn_kwargs,
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.PATCH_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.PATCH_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        call_fn_kwargs = dict(
            zone_name_or_id=self.module.params.get("zone_name_or_id"),
            domain=self.module.params.get("domain"),
            if_unmodified_since=self.module.params.get("if_unmodified_since"),
            view_id=self.module.params.get("view_id"),
            compartment_id=self.module.params.get("compartment_id"),
        )
        if self.module.params.get("scope") is not None:
            call_fn_kwargs["scope"] = self.module.params["scope"]
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_domain_records,
            call_fn_args=(),
            call_fn_kwargs=call_fn_kwargs,
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


class RrsetHelperCustom(DNSRecordsHelperCustom):
    def get_resource(self):
        if self.module.params.get("scope") is not None:
            return oci_common_utils.get_default_response_from_resource(
                oci_common_utils.list_all_resources(
                    self.client.get_rr_set,
                    zone_name_or_id=self.module.params.get("zone_name_or_id"),
                    domain=self.module.params.get("domain"),
                    rtype=self.module.params.get("rtype"),
                    view_id=self.module.params.get("view_id"),
                    scope=self.module.params.get("scope"),
                ).items
            )
        return oci_common_utils.get_default_response_from_resource(
            oci_common_utils.list_all_resources(
                self.client.get_rr_set,
                zone_name_or_id=self.module.params.get("zone_name_or_id"),
                domain=self.module.params.get("domain"),
                rtype=self.module.params.get("rtype"),
                view_id=self.module.params.get("view_id"),
            ).items
        )

    def update_resource(self):
        update_details = self.get_update_model()
        call_fn_kwargs = dict(
            zone_name_or_id=self.module.params.get("zone_name_or_id"),
            domain=self.module.params.get("domain"),
            rtype=self.module.params.get("rtype"),
            update_rr_set_details=update_details,
            if_unmodified_since=self.module.params.get("if_unmodified_since"),
            view_id=self.module.params.get("view_id"),
            compartment_id=self.module.params.get("compartment_id"),
        )
        if self.module.params.get("scope") is not None:
            call_fn_kwargs["scope"] = self.module.params["scope"]
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_rr_set,
            call_fn_args=(),
            call_fn_kwargs=call_fn_kwargs,
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def patch_resource(self):
        patch_details = self.get_patch_model()
        call_fn_kwargs = dict(
            zone_name_or_id=self.module.params.get("zone_name_or_id"),
            domain=self.module.params.get("domain"),
            rtype=self.module.params.get("rtype"),
            patch_rr_set_details=patch_details,
            if_unmodified_since=self.module.params.get("if_unmodified_since"),
            view_id=self.module.params.get("view_id"),
            compartment_id=self.module.params.get("compartment_id"),
        )
        if self.module.params.get("scope") is not None:
            call_fn_kwargs["scope"] = self.module.params["scope"]
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.patch_rr_set,
            call_fn_args=(),
            call_fn_kwargs=call_fn_kwargs,
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.PATCH_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.PATCH_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        call_fn_kwargs = dict(
            zone_name_or_id=self.module.params.get("zone_name_or_id"),
            domain=self.module.params.get("domain"),
            rtype=self.module.params.get("rtype"),
            if_unmodified_since=self.module.params.get("if_unmodified_since"),
            compartment_id=self.module.params.get("compartment_id"),
            view_id=self.module.params.get("view_id"),
        )
        if self.module.params.get("scope") is not None:
            call_fn_kwargs["scope"] = self.module.params["scope"]
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_rr_set,
            call_fn_args=(),
            call_fn_kwargs=call_fn_kwargs,
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


class SteeringPolicyHelperCustom:
    def get_resource(self):
        if self.module.params.get("scope") is not None:
            return oci_common_utils.call_with_backoff(
                self.client.get_steering_policy,
                steering_policy_id=self.module.params.get("steering_policy_id"),
                scope=self.module.params.get("scope"),
            )
        return super(SteeringPolicyHelperCustom, self).get_resource()

    def create_resource(self):
        create_details = self.get_create_model()
        call_fn_kwargs = dict(create_steering_policy_details=create_details,)
        if self.module.params.get("scope") is not None:
            call_fn_kwargs["scope"] = self.module.params["scope"]
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_steering_policy,
            call_fn_args=(),
            call_fn_kwargs=call_fn_kwargs,
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def update_resource(self):
        update_details = self.get_update_model()
        call_fn_kwargs = dict(
            steering_policy_id=self.module.params.get("steering_policy_id"),
            update_steering_policy_details=update_details,
            if_unmodified_since=self.module.params.get("if_unmodified_since"),
        )
        if self.module.params.get("scope") is not None:
            call_fn_kwargs["scope"] = self.module.params["scope"]
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_steering_policy,
            call_fn_args=(),
            call_fn_kwargs=call_fn_kwargs,
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        call_fn_kwargs = dict(
            steering_policy_id=self.module.params.get("steering_policy_id"),
            if_unmodified_since=self.module.params.get("if_unmodified_since"),
        )
        if self.module.params.get("scope") is not None:
            call_fn_kwargs["scope"] = self.module.params["scope"]
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_steering_policy,
            call_fn_args=(),
            call_fn_kwargs=call_fn_kwargs,
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


class SteeringPolicyAttachmentHelperCustom:
    def get_resource(self):
        if self.module.params.get("scope") is not None:
            return oci_common_utils.call_with_backoff(
                self.client.get_steering_policy_attachment,
                steering_policy_attachment_id=self.module.params.get(
                    "steering_policy_attachment_id"
                ),
                scope=self.module.params.get("scope"),
            )
        return super(SteeringPolicyAttachmentHelperCustom, self).get_resource()

    def create_resource(self):
        create_details = self.get_create_model()
        call_fn_kwargs = dict(create_steering_policy_attachment_details=create_details,)
        if self.module.params.get("scope") is not None:
            call_fn_kwargs["scope"] = self.module.params["scope"]
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_steering_policy_attachment,
            call_fn_args=(),
            call_fn_kwargs=call_fn_kwargs,
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def update_resource(self):
        update_details = self.get_update_model()
        call_fn_kwargs = dict(
            steering_policy_attachment_id=self.module.params.get(
                "steering_policy_attachment_id"
            ),
            update_steering_policy_attachment_details=update_details,
            if_unmodified_since=self.module.params.get("if_unmodified_since"),
        )
        if self.module.params.get("scope") is not None:
            call_fn_kwargs["scope"] = self.module.params["scope"]
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_steering_policy_attachment,
            call_fn_args=(),
            call_fn_kwargs=call_fn_kwargs,
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        call_fn_kwargs = dict(
            steering_policy_attachment_id=self.module.params.get(
                "steering_policy_attachment_id"
            ),
            if_unmodified_since=self.module.params.get("if_unmodified_since"),
        )
        if self.module.params.get("scope") is not None:
            call_fn_kwargs["scope"] = self.module.params["scope"]
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_steering_policy_attachment,
            call_fn_args=(),
            call_fn_kwargs=call_fn_kwargs,
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


class TsigKeyHelperCustom:
    def get_resource(self):
        if self.module.params.get("scope") is not None:
            return oci_common_utils.call_with_backoff(
                self.client.get_tsig_key,
                tsig_key_id=self.module.params.get("tsig_key_id"),
                scope=self.module.params.get("scope"),
            )

        return super(TsigKeyHelperCustom, self).get_resource()

    def create_resource(self):
        create_details = self.get_create_model()
        call_fn_kwargs = dict(create_tsig_key_details=create_details,)
        if self.module.params.get("scope") is not None:
            call_fn_kwargs["scope"] = self.module.params["scope"]
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_tsig_key,
            call_fn_args=(),
            call_fn_kwargs=call_fn_kwargs,
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def update_resource(self):
        update_details = self.get_update_model()
        call_fn_kwargs = dict(
            tsig_key_id=self.module.params.get("tsig_key_id"),
            update_tsig_key_details=update_details,
            if_unmodified_since=self.module.params.get("if_unmodified_since"),
        )
        if self.module.params.get("scope") is not None:
            call_fn_kwargs["scope"] = self.module.params["scope"]
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_tsig_key,
            call_fn_args=(),
            call_fn_kwargs=call_fn_kwargs,
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        call_fn_kwargs = dict(
            tsig_key_id=self.module.params.get("tsig_key_id"),
            if_unmodified_since=self.module.params.get("if_unmodified_since"),
        )
        if self.module.params.get("scope") is not None:
            call_fn_kwargs["scope"] = self.module.params["scope"]
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_tsig_key,
            call_fn_args=(),
            call_fn_kwargs=call_fn_kwargs,
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


class ViewHelperCustom:
    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_view,
            view_id=self.module.params.get("view_id"),
            scope=self.module.params.get("scope"),
        )

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_view,
            view_id=summary_model.id,
            scope=self.module.params.get("scope"),
        ).data


class ResolverHelperCustom:
    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_resolver,
            resolver_id=self.module.params.get("resolver_id"),
            scope=self.module.params.get("scope"),
        )

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_resolver,
            resolver_id=summary_model.id,
            scope=self.module.params.get("scope"),
        ).data


class ResolverEndpointHelperCustom:
    def get_resource(self):
        # The API endpoint for getting endpoint intermittently fails with 404. CLI has the same issue as well so it
        # should be an API issue. The console uses the get_resolver endpoint to get the details of endpoints as well.
        # So using the same here as well.
        resolver = oci_common_utils.call_with_backoff(
            self.client.get_resolver,
            resolver_id=self.module.params.get("resolver_id"),
            scope=self.module.params.get("scope"),
        ).data
        endpoints = resolver.endpoints or []
        for endpoint in endpoints:
            if endpoint.name == self.module.params.get("name"):
                return oci_common_utils.get_default_response_from_resource(
                    resource=self.get_get_model_from_summary_model(endpoint)
                )
        return oci_common_utils.raise_does_not_exist_service_error()

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_resolver_endpoint,
            resolver_id=self.module.params.get("resolver_id"),
            resolver_endpoint_name=summary_model.name,
            scope=self.module.params.get("scope"),
        ).data
