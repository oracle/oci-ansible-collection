# Copyright (c) 2020 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils

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
    pass


class DomainRecordsHelperCustom(DNSRecordsHelperCustom):
    pass


class RrsetHelperCustom(DNSRecordsHelperCustom):
    pass
