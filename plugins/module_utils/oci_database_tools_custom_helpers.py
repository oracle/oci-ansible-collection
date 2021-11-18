from __future__ import absolute_import, division, print_function

__metaclass__ = type


class DatabaseToolsConnectionHelperCustom:
    def get_optional_kwargs_for_list(self):
        """
        create operation uses list_resources call which requires the `type` to be a list
        refer: https://bitbucket.oci.oraclecorp.com/projects/ANSI/repos/oci-ansible-collection/pull-requests/184/overview
        """
        optional_kwargs_for_list = super(
            DatabaseToolsConnectionHelperCustom, self
        ).get_optional_kwargs_for_list()
        if "type" in optional_kwargs_for_list.keys():
            existing_value = optional_kwargs_for_list.get("type")
            optional_kwargs_for_list["type"] = [existing_value]
        return optional_kwargs_for_list
