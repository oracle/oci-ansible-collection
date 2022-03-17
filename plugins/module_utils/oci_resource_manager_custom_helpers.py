# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from base64 import b64encode


def get_base64_encoded_stack_tf_config(client, stack_id):
    response = oci_common_utils.call_with_backoff(
        client.get_stack_tf_config, stack_id=stack_id
    ).data
    return b64encode(response.content).decode("ascii")


def get_base64_encoded_template_tf_config(client, template_id):
    """
    Get base 64 encoded terraform config zip file for a template.

    @param client: ResourceManagerClient
    @param template_id: str - OCID for template id
    :returns: str (ascii) base 64 encoded terraform zip file
    """
    response = oci_common_utils.call_with_backoff(
        client.get_template_tf_config, template_id=template_id
    ).data
    return b64encode(response.content).decode("ascii")


class StackHelperCustom:
    def get_exclude_attributes(self):
        """
        config_source.template_id, config_source.zip_file_base64_encoded are not present in the
        GET return model so these properties are added as exclude_attributes in the generated module. but we are setting
        these properties  in the get_existing_resource_dict_for_idempotence_check() to the existing resource dict
        so these properties can be compared during idempotence check
        """
        exclude_attributes = super(StackHelperCustom, self).get_exclude_attributes()
        remove_exclude_attributes = [
            "config_source.template_id",
            "config_source.zip_file_base64_encoded",
        ]
        exclude_attributes = [
            x for x in exclude_attributes if x not in remove_exclude_attributes
        ]
        return exclude_attributes

    def get_existing_resource_dict_for_idempotence_check(self, existing_resource):
        existing_resource_dict = super(
            StackHelperCustom, self
        ).get_existing_resource_dict_for_idempotence_check(existing_resource)
        if self.module.params.get(
            "key_by"
        ) and "config_source" not in self.module.params.get("key_by"):
            return existing_resource_dict
        if (
            existing_resource_dict.get("config_source")
            and existing_resource_dict.get("config_source").get("config_source_type")
            == "ZIP_UPLOAD"
            and self.module.params.get("config_source")
        ):
            stack_tf_config = get_base64_encoded_stack_tf_config(
                self.client, existing_resource_dict.get("id")
            )

            # Compare the tf config of the existing stack against the
            # tf config of the template being used to create the new one.
            if self.module.params.get("config_source").get(
                "config_source_type"
            ) == "TEMPLATE_CONFIG_SOURCE" and self.module.params.get(
                "config_source"
            ).get(
                "template_id"
            ):
                template_id = self.module.params.get("config_source").get("template_id")
                template_tf_config = get_base64_encoded_template_tf_config(
                    self.client, template_id
                )
                if stack_tf_config == template_tf_config:
                    # tf configs match, populate the existing resource dict, i.e. the get model
                    # with the template id similar to the create model for new resource
                    existing_resource_dict["config_source"][
                        "config_source_type"
                    ] = "TEMPLATE_CONFIG_SOURCE"
                    existing_resource_dict["config_source"]["template_id"] = template_id
            elif self.module.params.get("config_source").get(
                "config_source_type"
            ) == "ZIP_UPLOAD" and self.module.params.get("config_source").get(
                "zip_file_base64_encoded"
            ):
                existing_resource_dict["config_source"][
                    "zip_file_base64_encoded"
                ] = stack_tf_config
        return existing_resource_dict

    def get_existing_resource_dict_for_update(self):
        existing_resource_dict = super(
            StackHelperCustom, self
        ).get_existing_resource_dict_for_update()
        if (
            self.module.params.get("config_source")
            and self.module.params.get("config_source").get("zip_file_base64_encoded")
            and existing_resource_dict.get("config_source")
            and existing_resource_dict.get("config_source").get("config_source_type")
            == "ZIP_UPLOAD"
        ):
            existing_resource_dict["config_source"][
                "zip_file_base64_encoded"
            ] = get_base64_encoded_stack_tf_config(
                self.client, existing_resource_dict.get("id")
            )
        return existing_resource_dict


class JobHelperCustom:
    # Creating a job is not an idempotent operation. It might not be possible to determine if there were any changes
    # done to the stack itself (terraform config can be updated). So I don't think there is a reliable way for ansible
    # to determine if a job actually needs to run or not. Also it is perfectly valid to run some (for ex: plan) jobs
    # multiple times. I think it is safe to rely on terraform since it anyway performs actions based on changes and
    # try not to implement what terraform already does in ansible which might not be possible in most of the cases.
    def get_matching_resource(self):
        return None

    def is_resource_dead(self, resource):
        if resource.lifecycle_state == "CANCELED":
            return True

        return False


class TemplateHelperCustom:
    """
    Custom helper for Resource Manager Template resource.
    """

    def list_resources(self):
        """
        Overrides the generated list_resources to include
        the template_category_id param.

        Category '3' implies 'Private Templates'.
        """

        try:
            orig_category_id = self.module.params.get("template_category_id")
            self.module.params["template_category_id"] = "3"
            return super(TemplateHelperCustom, self).list_resources()
        finally:
            self.module.params["template_category_id"] = orig_category_id

    def get_required_kwargs_for_list(self):
        """
        Populates the required keyword agruments
        from the module's params.
        """

        required_list_method_params = ["template_category_id"]

        return dict(
            (param, self.module.params[param])
            for param in required_list_method_params
            if self.module.params.get(param) is not None
        )

    def get_existing_resource_dict_for_idempotence_check(self, existing_resource):
        """
        Overrides the generated method to include logo file and template zip
        file in the existing_resource.
        """

        existing_resource_dict = super(
            TemplateHelperCustom, self
        ).get_existing_resource_dict_for_idempotence_check(existing_resource)

        existing_resource_dict = self.enrich_resource_dict_with_logo_file(
            existing_resource_dict
        )

        existing_resource_dict = self.enrich_resource_dict_with_config_zip_file(
            existing_resource_dict
        )

        return existing_resource_dict

    def get_existing_resource_dict_for_update(self):
        """
        Overrides the generated method to include logo file and template zip
        file in the existing_resource for the update scenario
        """

        existing_resource_dict = super(
            TemplateHelperCustom, self
        ).get_existing_resource_dict_for_update()

        existing_resource_dict = self.enrich_resource_dict_with_logo_file(
            existing_resource_dict
        )

        existing_resource_dict = self.enrich_resource_dict_with_config_zip_file(
            existing_resource_dict
        )

        return existing_resource_dict

    def enrich_resource_dict_with_logo_file(self, existing_resource_dict):
        """
        Enriches the existing_resource_dict with the logo file.
        """

        if existing_resource_dict.get("id") and not existing_resource_dict.get(
            "logo_file_base64_encoded"
        ):
            existing_resource_dict[
                "logo_file_base64_encoded"
            ] = self.get_base64_encoded_template_logo(existing_resource_dict["id"])
        return existing_resource_dict

    def enrich_resource_dict_with_config_zip_file(self, existing_resource_dict):
        """
        Enriches the existing_resource_dict with the template zip file.
        """

        config_source = existing_resource_dict.get("template_config_source")
        if (
            existing_resource_dict.get("id")
            and config_source
            and config_source.get("template_config_source_type") == "ZIP_UPLOAD"
            and not config_source.get("zip_file_base64_encoded")
        ):
            existing_resource_dict["template_config_source"][
                "zip_file_base64_encoded"
            ] = self.get_base64_encoded_template_tf_config(existing_resource_dict["id"])

        return existing_resource_dict

    def get_base64_encoded_template_tf_config(self, template_id):
        """
        Fetch the template tf config zip file for the
        specified template id.
        """

        response = oci_common_utils.call_with_backoff(
            self.client.get_template_tf_config, template_id
        ).data
        return b64encode(response.content).decode("ascii")

    def get_base64_encoded_template_logo(self, template_id):
        """
        Fetch the template logo file for the
        specified template id.
        """

        response = oci_common_utils.call_with_backoff(
            self.client.get_template_logo, template_id
        ).data
        return b64encode(response.content).decode("ascii")

    def get_exclude_attributes(self):
        """
        Overriding the method to remove logo_file_base64_encoded
        from the excluded attributes.

        logo_file_base64_encoded will not be ignored during idempotence
        check as we are populating the required data in
        get_existing_resource_dict_for_update method.
        """
        exclude_attributes = super(TemplateHelperCustom, self).get_exclude_attributes()

        remove_exclude_attributes = [
            "logo_file_base64_encoded",
            "template_config_source.zip_file_base64_encoded",
        ]
        exclude_attributes = [
            x for x in exclude_attributes if x not in remove_exclude_attributes
        ]

        return exclude_attributes
