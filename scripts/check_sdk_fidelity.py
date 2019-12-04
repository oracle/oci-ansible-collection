#!/usr/bin/env python
# coding: utf-8
# Copyright (c) 2018, Oracle and/or its affiliates. All rights reserved.

import collections
import importlib
import inspect
import os
import pickle
import pkgutil
import re
import tempfile

import oci
import q
import yaml


# Finds all the gaps (unimplemented features/params) between the OCI ansible modules and the OCI Python SDK

def nested_dict():
    return collections.defaultdict(nested_dict)


class AnsibleModuleMetadata:
    ANSIBLE_CLOUD_MODULES_PKG = "ansible.modules.cloud.oracle"

    def __init__(self, force=False):
        self.ansible_module_opts = nested_dict()
        self.force = force
        self._populate_metadata()

    def _populate_metadata(self):
        ansible_metadata_cache_file_name = os.path.join(tempfile.gettempdir(), "oci-ansible-metadata.cache")
        if self.force or not os.path.isfile(ansible_metadata_cache_file_name):
            for name in AnsibleModuleMetadata.get_all_ansible_modules():
                # One strategy is to load options from the Ansible modules' documentation snippet as shown in this
                # comment below, yet this doesn't appear to handle documentation_fragments. The correct approach would
                # be to load doc fragments too, and then get effective module_opts.
                #
                # ansible_module = AnsibleModuleMetadata.load_module(name)
                # module_doc = yaml.safe_load(ansible_module.DOCUMENTATION)
                # if 'options' in module_doc:
                #     module_opts = module_doc['options']
                #     self.ansible_module_opts[ansible_module.__name__]['options'] = module_opts

                # HACK: For now just parse ansible-doc output to find options supported by a module, and merge options
                # discovered through DOCUMENTATION
                import subprocess
                command = 'ansible-doc %s|grep "^[-=] .*" | grep -v "^- name: "|sed "s@^[-=] @@g"' % name
                output = subprocess.check_output(command, shell=True)
                module_opts = output.decode('utf-8').strip().splitlines()
                module_opts = [a.strip() for a in module_opts]
                if module_opts:
                    ansible_module_name = AnsibleModuleMetadata.ANSIBLE_CLOUD_MODULES_PKG + "." + name
                    q(ansible_module_name, module_opts)
                    self.ansible_module_opts[ansible_module_name]['options'] = module_opts

                # Parsing 'params' from ansible-doc doesn't give us suboptions easily. So get that from DOCUMENTATION
                # and merge
                ansible_module = AnsibleModuleMetadata.load_module(name)
                module_doc = yaml.safe_load(ansible_module.DOCUMENTATION)
                module_opts_from_doc = []
                if 'options' in module_doc:
                    module_opts = module_doc['options']
                    for k in module_opts.keys():
                        if 'suboptions' in module_opts[k]:
                            subopts = module_opts[k]['suboptions']
                            module_opts_from_doc.extend(subopts.keys())
                        else:
                            module_opts_from_doc.append(k)
                        # also include aliases in the final list
                        if 'aliases' in module_opts[k]:
                            module_opts_from_doc.extend(module_opts[k]['aliases'])
                # merge module_opts_from_doc to the values discovered from ansible-doc
                curr_val = self.ansible_module_opts[ansible_module_name]['options']
                if curr_val is not None:
                    curr_val.extend(module_opts_from_doc)
                else:
                    curr_val = module_opts_from_doc
                self.ansible_module_opts[ansible_module_name]['options'] = set(curr_val)

            # write latest metadata to cache
            with open(ansible_metadata_cache_file_name, 'wb') as amcf:
                pickle.dump(self.ansible_module_opts, amcf)
        else:
            # load metadata from cache
            with open(ansible_metadata_cache_file_name, 'rb') as amcf:
                self.ansible_module_opts = pickle.load(amcf)

    @staticmethod
    def load_module(ansible_module_name):
        return importlib.import_module(AnsibleModuleMetadata.ANSIBLE_CLOUD_MODULES_PKG + "." + ansible_module_name)

    @staticmethod
    def get_all_ansible_modules():
        # get all ansible modules under ANSIBLE_CLOUD_MODULES_PKG that do not start with "_"
        ansible_mod = importlib.import_module(AnsibleModuleMetadata.ANSIBLE_CLOUD_MODULES_PKG).__path__
        return [modname for _, modname, is_pkg in pkgutil.iter_modules(ansible_mod) if not is_pkg
                and re.match(r'^oci_.*$', modname)]

    def get_module_options(self):
        return self.ansible_module_opts

    def get_ansible_mods_referring_svc_mthds(self, mod, client_class, method_name):
        # A naive implementation to find the ansible module that refers a service client. It just loads the ansible
        # module source and checks if the names of the service module, client_class and method_name are present
        # in the file.
        matching_modules = []
        for name in self.get_all_ansible_modules():
            module = self.load_module(name)
            with open(module.__file__, 'r') as f:
                content = f.read()
                import_pattern = "import %s" % (client_class)
                pattern = "%s\W" % method_name
                if client_class in content and method_name in content and import_pattern in content and re.findall(
                        pattern, content, re.MULTILINE):
                    matching_modules.append(module.__name__)
        return matching_modules

    @staticmethod
    def is_fact_module(ansible_module_name):
        return ansible_module_name.endswith("_facts")

    @staticmethod
    def get_raw_ansible_module_name(ansible_module_fqdn):
        return ansible_module_fqdn.replace(AnsibleModuleMetadata.ANSIBLE_CLOUD_MODULES_PKG + ".", "")


class ServiceMetadata:
    OCI_PKG = "oci."

    def __init__(self, filter_module=None, force=False):
        self.meth_attrs = nested_dict()
        self.force = force
        self.filter_module = filter_module
        self._populate_metadata()

    @staticmethod
    def get_client_classes_in_module(name):
        # Get all client classes in a module by matching for all *Client classes that are members of this root module
        all_clients = [t[1] for t in
                       inspect.getmembers(inspect.getmodule(importlib.import_module(ServiceMetadata.OCI_PKG + name))) if
                       re.match(r'.*Client', t[0]) and not re.match('.*CompositeOperations', t[0])]
        return all_clients

    def _populate_metadata(self):
        service_metadata_cache_file_name = os.path.join(tempfile.gettempdir(),
                                                        "oci-service-metadata-" + oci.__version__ + ".cache")
        if self.force or not os.path.isfile(service_metadata_cache_file_name):
            # populate meth_attrs
            for mod_name in ServiceMetadata.get_all_oci_modules():
                if self.filter_module is None or self.filter_module == mod_name:
                    for client_class in ServiceMetadata.get_client_classes_in_module(mod_name):
                        [self._process_method(client_class, meth) for meth in
                         ServiceMetadata.get_list_methods(client_class)]
                        [self._process_method(client_class, meth) for meth in
                         ServiceMetadata.get_modify_methods(client_class)]
            # write to cache
            with open(service_metadata_cache_file_name, 'wb') as smcf:
                pickle.dump(self.meth_attrs, smcf)
        else:
            with open(service_metadata_cache_file_name, 'rb') as smcf:
                self.meth_attrs = pickle.load(smcf)

    @staticmethod
    def get_list_methods(client_class):
        return [meth for meth in dir(client_class) if callable(getattr(client_class, meth)) and
                ServiceMetadata.is_a_list_method(meth)]

    @staticmethod
    def get_modify_methods(client_class):
        return [meth for meth in dir(client_class) if callable(getattr(client_class, meth)) and
                ServiceMetadata.is_a_modify_method(meth)]

    @staticmethod
    def is_a_list_method(method):
        list_method_prefixes = ['list', 'get']
        return any(method.startswith(prefix + "_") for prefix in list_method_prefixes)

    @staticmethod
    def is_a_modify_method(method):
        modify_method_prefixes = ['create', 'update', 'delete', 'terminate', 'launch']
        return any(method.startswith(prefix + "_") for prefix in modify_method_prefixes)

    def _process_method(self, client_class, meth):
        method_attrs = self._get_method_params(client_class, meth)
        # each list item is of form "<type> <param_name>"
        if method_attrs:
            for attr in method_attrs:
                (param_type, param_name) = attr.split(' ')
                q(param_type, param_name)
                built_in_type = ['str', 'bool', 'obj', 'int', 'datetime', 'list[str]']
                if any(param_type == p for p in built_in_type):
                    q(client_class.__module__, client_class.__qualname__, meth, param_name)
                    self._add_to_meth_attrs(str(client_class.__module__), str(client_class.__qualname__), meth,
                                            param_name)
                else:
                    q("recursively finding attributes for ", param_type)
                    client_class_module = importlib.import_module(client_class.__module__)
                    client_class_package = importlib.import_module(client_class_module.__package__)
                    models_module_in_client_class_package = client_class_package.models
                    model_class = getattr(models_module_in_client_class_package, param_type)
                    init_attrs = self._get_method_params(model_class, "__init__")
                    q(client_class.__module__, client_class.__qualname__, meth, init_attrs)
                    for init_attr in init_attrs:
                        self._add_to_meth_attrs(str(client_class.__module__), str(client_class.__qualname__), meth,
                                                init_attr)

    def _add_to_meth_attrs(self, module_name, class_name, meth, attr):
        if self.meth_attrs[module_name][class_name][meth]:
            self.meth_attrs[module_name][class_name][meth].append(attr)
        else:
            self.meth_attrs[module_name][class_name][meth] = [attr]

    def _get_method_params(self, client_class, meth):
        import subprocess
        ignore_params = ["limit", "retry_strategy", "page", "sort_by", "sort_order", "opc_request_id",
                         "opc_client_request_id", "opc_retry_token", "if_match"]
        ignore_pattern = "\|".join(ignore_params)
        command = 'python -c "import inspect; import oci; print(inspect.getdoc(%s.%s.%s))" | ' \
                  'grep ":param.*$" | grep -v "%s" | cut -d":" -f2 | sed "s@param @@g"' % (client_class.__module__,
                                                                                           client_class.__qualname__,
                                                                                           meth, ignore_pattern)
        q(command)

        output = subprocess.check_output(command, shell=True)
        method_params = output.decode('utf-8').strip().splitlines()
        return [a.strip() for a in method_params]

    @staticmethod
    def get_all_oci_modules():
        # get all modules under oci that do not start with "_"
        return [modname for _, modname, is_pkg in pkgutil.iter_modules(oci.__path__) if
                is_pkg and not re.match(r'^_.*', modname)]

    def get_meth_attrs(self):
        return self.meth_attrs


# These fact modules reference bridge class (classes that span two or more services
# ans lack certain params, so excluding those attributes
FACTS_EXCLUDES = {"oci_volume_facts": ['instance_id'],
                  "oci_boot_volume_facts": ['instance_id'],
                  "oci_instance_facts": ['boot_volume_id', 'volume_id'],
                  "oci_group_facts": ['user_id'],
                  "oci_user_facts": ['group_id']}
EXCLUDES = {  # as size_in_mbs is deprecated, we provide size_in_gbs instead
    "oci_volume": ['size_in_mbs'],
    # as zone_name_or_id is split into zone_name and id
    # we accept patch_items and update_items instead of a single alias items
    "oci_zone_records": ["zone_name_or_id", "items"],
    "oci_zone": ["zone_name_or_id"],
    "oci_domain_records": ["zone_name_or_id", "items"],
    "oci_rrset": ["zone_name_or_id", "items"],
    # XXX: check LB, DB and Casper modules
}


def is_excluded(ansible_module_name, option_name):
    if AnsibleModuleMetadata.is_fact_module(ansible_module_name):
        ansible_mod_exemptions = FACTS_EXCLUDES.get(ansible_module_name)
    else:
        ansible_mod_exemptions = EXCLUDES.get(ansible_module_name)

    q("exemptions for ansible module", ansible_module_name, ansible_mod_exemptions)
    if ansible_mod_exemptions:
        return option_name in ansible_mod_exemptions
    return False


def find_gaps_in_facts_modules():
    sm = ServiceMetadata()
    am = AnsibleModuleMetadata()

    gaps = []

    for oci_mod in sm.get_all_oci_modules():
        for client in sm.get_client_classes_in_module(oci_mod):
            module_name = client.__module__
            client_class = client.__qualname__
            for method in sm.get_list_methods(client):
                if method.startswith("list_"):  # only check against list_* methods;
                    method_params = sm.get_meth_attrs()[module_name][client_class][method]
                    q(module_name, client_class, method, method_params)

                    ansible_mods_referrers = am.get_ansible_mods_referring_svc_mthds(module_name, client_class,
                                                                                             method)
                    q(ansible_mods_referrers)

                    for ansible_mod in ansible_mods_referrers:
                        if AnsibleModuleMetadata.is_fact_module(ansible_mod):  # match only fact modules
                            fact_module_options = am.get_module_options()[ansible_mod]['options']
                            for attr in method_params:
                                if attr not in fact_module_options and \
                                        not is_excluded(am.get_raw_ansible_module_name(ansible_mod), attr):
                                    err_msg = ("`%s`: '%s' not supported as a module option.  %s.%s:%s supports "
                                               "an attribute named '%s'." % (
                                                   am.get_raw_ansible_module_name(ansible_mod), attr, module_name,
                                                   client_class, method, attr))
                                    gaps.append(err_msg)
    return gaps


def find_gaps_in_resource_modules():
    sm = ServiceMetadata()
    am = AnsibleModuleMetadata()

    gaps = []

    for oci_mod in sm.get_all_oci_modules():
        for client in sm.get_client_classes_in_module(oci_mod):
            module_name = client.__module__
            client_class = client.__qualname__
            for meth_name in sm.get_meth_attrs()[module_name][client_class]:
                if ServiceMetadata.is_a_modify_method(meth_name):
                    meth_attrs = sm.get_meth_attrs()[module_name][client_class][meth_name]
                    ansible_mod_referrers = am.get_ansible_mods_referring_svc_mthds(module_name, client_class,
                                                                                            meth_name)

                    for ansible_mod in ansible_mod_referrers:
                        if not AnsibleModuleMetadata.is_fact_module(ansible_mod):  # only match against resource modules
                            resource_module_options = am.get_module_options()[ansible_mod]['options']
                            for attr in meth_attrs:
                                if attr not in resource_module_options and \
                                        not is_excluded(am.get_raw_ansible_module_name(ansible_mod), attr):
                                    err_msg = ("`%s`: '%s' not supported as a module option.  %s.%s.%s supports an "
                                               "attribute named '%s'." % (
                                                   am.get_raw_ansible_module_name(ansible_mod), attr, module_name,
                                                   client_class, meth_name, attr))
                                    gaps.append(err_msg)

    return gaps


def find_unsupported_resource_methods():
    """
    Find all unsupported resource methods. Found by detecting methods in Service client classes that have not been
    called by any OCI Ansible module
    :return: List of gaps
    """
    sm = ServiceMetadata()
    am = AnsibleModuleMetadata()

    gaps_dict = nested_dict()
    for oci_mod in sm.get_all_oci_modules():
        for client in sm.get_client_classes_in_module(oci_mod):
            module_name = client.__module__
            client_class = client.__qualname__
            for meth_name in sm.get_meth_attrs()[module_name][client_class]:
                if ServiceMetadata.is_a_modify_method(meth_name) or ServiceMetadata.is_a_list_method(meth_name):
                    ansible_mod_referrers = am.get_ansible_mods_referring_svc_mthds(module_name, client_class,
                                                                                            meth_name)
                    if len(ansible_mod_referrers) == 0:
                        err_msg = "`%s.%s.%s` not yet implemented" % (module_name, client_class, meth_name)
                        curr = gaps_dict[module_name][client_class]
                        if len(curr) == 0:
                            curr = []
                        curr.append(meth_name)
                        gaps_dict[module_name][client_class] = curr
    return gaps_dict


def find_gaps_in_return_block():
    sm = ServiceMetadata()
    am = AnsibleModuleMetadata()

    gaps = []
    for oci_mod in sm.get_all_oci_modules():
        for client in sm.get_client_classes_in_module(oci_mod):
            module_name = client.__module__
            client_class = client.__qualname__
            for meth_name in sm.get_meth_attrs()[module_name][client_class]:
                if ServiceMetadata.is_a_modify_method(meth_name) or ServiceMetadata.is_a_list_method(meth_name):
                    ansible_mod_referrers = am.get_ansible_mods_referring_svc_mthds(module_name, client_class,
                                                                                            meth_name)
                    for ansible_mod in ansible_mod_referrers:
                        m = am.load_module(ansible_mod)
                        return_block = yaml.safe_load(m.RETURN)
                        # XXX: Our return blocks are not consistently formatted today
                        # and so we can't process them uniformly
    return gaps


def main():
    # _test()
    lint()


def lint():
    facts_gaps = find_gaps_in_facts_modules()
    _print_gaps(facts_gaps, "Gaps in facts modules")

    resource_modules_gaps = find_gaps_in_resource_modules()
    _print_gaps(resource_modules_gaps, "Gaps in resource modules")

    unsupported_res_methods = find_unsupported_resource_methods()
    print("# Unsupported resource methods")
    for mod_name in unsupported_res_methods.keys():
        print("\n- `" + mod_name + "`")
        for client_class in unsupported_res_methods[mod_name].keys():
            print("  - `" + client_class + "`")
            for meth in unsupported_res_methods[mod_name][client_class]:
                print("    - " + meth)

    # return_block_gaps = find_gaps_in_return_block()
    # _print_gaps(return_block_gaps, "TODO - WIP - Gaps in return block of OCI ansible modules")

    # choose return code based on if any gaps were found
    # for now only consider facts_gaps.
    # any_gaps = any(len(g) > 0 for g in [facts_gaps])
    # ret_code = 0
    # if any_gaps:
    #     ret_code = 1
    # sys.exit(ret_code)


def _print_gaps(gaps, description):
    print("# " + description)
    if gaps:
        for g in gaps:
            print("- " + g)
    print()


def _test():
    sm = ServiceMetadata()

    import pprint
    pprint.pprint(sm.get_meth_attrs()["oci.core.blockstorage_client"]["BlockstorageClient"]["create_volume"])

    pprint.pprint(sm.get_meth_attrs()["oci.core.blockstorage_client"]["BlockstorageClient"]["list_volumes"])
    pprint.pprint(sm.get_meth_attrs()["oci.core.blockstorage_client"]["BlockstorageClient"]["get_volume"])

    am = AnsibleModuleMetadata()
    pprint.pprint(am.get_module_options()[AnsibleModuleMetadata.ANSIBLE_CLOUD_MODULES_PKG + ".oci_instance"]['options'])


main()
