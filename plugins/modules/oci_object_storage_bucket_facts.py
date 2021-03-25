#!/usr/bin/python
# Copyright (c) 2017, 2021 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.
# GENERATED FILE - DO NOT EDIT - MANUAL CHANGES WILL BE OVERWRITTEN


from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_object_storage_bucket_facts
short_description: Fetches details about one or multiple Bucket resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Bucket resources in Oracle Cloud Infrastructure
    - Gets a list of all BucketSummary items in a compartment. A BucketSummary contains only summary fields for the bucket
      and does not contain fields like the user-defined metadata.
    - ListBuckets returns a BucketSummary containing at most 1000 buckets. To paginate through more buckets, use the returned
      `opc-next-page` value with the `page` request parameter.
    - To use this and other API operations, you must be authorized in an IAM policy. If you are not authorized,
      talk to an administrator. If you are an administrator who needs to write policies to give users access, see
      L(Getting Started with Policies,https://docs.cloud.oracle.com/Content/Identity/Concepts/policygetstarted.htm).
    - If I(bucket_name) is specified, the details of a single Bucket will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    namespace_name:
        description:
            - The Object Storage namespace used for the request.
        type: str
        required: true
    bucket_name:
        description:
            - "The name of the bucket. Avoid entering confidential information.
              Example: `my-new-bucket1`"
            - Required to get a specific bucket.
        type: str
    fields:
        description:
            - Bucket summary includes the 'namespace', 'name', 'compartmentId', 'createdBy', 'timeCreated',
              and 'etag' fields. This parameter can also include 'approximateCount' (approximate number of objects) and 'approximateSize'
              (total approximate size in bytes of all objects). For example 'approximateCount,approximateSize'.
        type: list
        choices:
            - "approximateCount"
            - "approximateSize"
            - "tags"
    compartment_id:
        description:
            - The ID of the compartment in which to list buckets.
            - Required to list multiple buckets.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List buckets
  oci_object_storage_bucket_facts:
    namespace_name: namespace_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

- name: Get a specific bucket
  oci_object_storage_bucket_facts:
    namespace_name: namespace_name_example
    bucket_name: my-new-bucket1

"""

RETURN = """
buckets:
    description:
        - List of Bucket resources
    returned: on success
    type: complex
    contains:
        namespace:
            description:
                - The Object Storage namespace in which the bucket resides.
            returned: on success
            type: string
            sample: namespace_example
        name:
            description:
                - "The name of the bucket. Avoid entering confidential information.
                  Example: my-new-bucket1"
            returned: on success
            type: string
            sample: name_example
        compartment_id:
            description:
                - The compartment ID in which the bucket is authorized.
            returned: on success
            type: string
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        metadata:
            description:
                - Arbitrary string keys and values for user-defined metadata.
            returned: on success
            type: dict
            sample: {}
        created_by:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the user who created the bucket.
            returned: on success
            type: string
            sample: created_by_example
        time_created:
            description:
                - The date and time the bucket was created, as described in L(RFC 2616,https://tools.ietf.org/html/rfc2616#section-14.29).
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        etag:
            description:
                - The entity tag (ETag) for the bucket.
            returned: on success
            type: string
            sample: etag_example
        public_access_type:
            description:
                - The type of public access enabled on this bucket.
                  A bucket is set to `NoPublicAccess` by default, which only allows an authenticated caller to access the
                  bucket and its contents. When `ObjectRead` is enabled on the bucket, public access is allowed for the
                  `GetObject`, `HeadObject`, and `ListObjects` operations. When `ObjectReadWithoutList` is enabled on the
                  bucket, public access is allowed for the `GetObject` and `HeadObject` operations.
            returned: on success
            type: string
            sample: NoPublicAccess
        storage_tier:
            description:
                - The storage tier type assigned to the bucket. A bucket is set to `Standard` tier by default, which means
                  objects uploaded or copied to the bucket will be in the standard storage tier. When the `Archive` tier type
                  is set explicitly for a bucket, objects uploaded or copied to the bucket will be stored in archive storage.
                  The `storageTier` property is immutable after bucket is created.
            returned: on success
            type: string
            sample: Standard
        object_events_enabled:
            description:
                - Whether or not events are emitted for object state changes in this bucket. By default, `objectEventsEnabled` is
                  set to `false`. Set `objectEventsEnabled` to `true` to emit events for object state changes. For more information
                  about events, see L(Overview of Events,https://docs.cloud.oracle.com/Content/Events/Concepts/eventsoverview.htm).
            returned: on success
            type: bool
            sample: true
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        kms_key_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of a master encryption key used to call the Key Management
                  service to generate a data encryption key or to encrypt or decrypt a data encryption key.
            returned: on success
            type: string
            sample: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
        object_lifecycle_policy_etag:
            description:
                - The entity tag (ETag) for the live object lifecycle policy on the bucket.
            returned: on success
            type: string
            sample: object_lifecycle_policy_etag_example
        approximate_count:
            description:
                - The approximate number of objects in the bucket. Count statistics are reported periodically. You will see a
                  lag between what is displayed and the actual object count.
            returned: on success
            type: int
            sample: 56
        approximate_size:
            description:
                - The approximate total size in bytes of all objects in the bucket. Size statistics are reported periodically. You will
                  see a lag between what is displayed and the actual size of the bucket.
            returned: on success
            type: int
            sample: 56
        replication_enabled:
            description:
                - Whether or not this bucket is a replication source. By default, `replicationEnabled` is set to `false`. This will
                  be set to 'true' when you create a replication policy for the bucket.
            returned: on success
            type: bool
            sample: true
        is_read_only:
            description:
                - Whether or not this bucket is read only. By default, `isReadOnly` is set to `false`. This will
                  be set to 'true' when this bucket is configured as a destination in a replication policy.
            returned: on success
            type: bool
            sample: true
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the bucket.
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        versioning:
            description:
                - The versioning status on the bucket. A bucket is created with versioning `Disabled` by default.
                  For versioning `Enabled`, objects are protected from overwrites and deletes, by maintaining their version history. When versioning is
                  `Suspended`, the previous versions will still remain but new versions will no longer be created when overwitten or deleted.
            returned: on success
            type: string
            sample: Enabled
    sample: [{
        "namespace": "namespace_example",
        "name": "name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "metadata": {},
        "created_by": "created_by_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "etag": "etag_example",
        "public_access_type": "NoPublicAccess",
        "storage_tier": "Standard",
        "object_events_enabled": true,
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "kms_key_id": "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx",
        "object_lifecycle_policy_etag": "object_lifecycle_policy_etag_example",
        "approximate_count": 56,
        "approximate_size": 56,
        "replication_enabled": true,
        "is_read_only": true,
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "versioning": "Enabled"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.object_storage import ObjectStorageClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BucketFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "namespace_name",
            "bucket_name",
        ]

    def get_required_params_for_list(self):
        return [
            "namespace_name",
            "compartment_id",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "fields",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_bucket,
            namespace_name=self.module.params.get("namespace_name"),
            bucket_name=self.module.params.get("bucket_name"),
            **optional_kwargs
        )

    def list_resources(self):
        optional_list_method_params = [
            "fields",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_buckets,
            namespace_name=self.module.params.get("namespace_name"),
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


BucketFactsHelperCustom = get_custom_class("BucketFactsHelperCustom")


class ResourceFactsHelper(BucketFactsHelperCustom, BucketFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            namespace_name=dict(type="str", required=True),
            bucket_name=dict(type="str"),
            fields=dict(
                type="list", choices=["approximateCount", "approximateSize", "tags"]
            ),
            compartment_id=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="bucket",
        service_client_class=ObjectStorageClient,
        namespace="object_storage",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(buckets=result)


if __name__ == "__main__":
    main()
