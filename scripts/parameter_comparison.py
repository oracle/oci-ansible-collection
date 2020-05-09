# How to run:
# Update variables in section: USER TO UPDATE
# python parameter_comparison.py
#
# Notes:
# - Does not handle nested parameters at all, will only alert if top level params mismatch
# - Only detects mismatches in module parameters (no code logic)
# - Does not detect differeces in "choices" for enum params
# - Only examines DOCUMENTATION block, does not check RETURN values

import yaml
import six
import ntpath
import os

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

separator = "==============================================================================================================================="

# we try to find which old modules do not have matching new modules
# we explicitly want to ignore services that we know aren't implmented yet because
# we know those modules wont have a match
# if an entry is missing here, you will just end up with more noise in the
# 'old modules with no matching new module' list
SERVICES_NOT_YET_IMPLEMENTED_IN_NEW_MODULES = [
    "email",
    "dns",
    "database",
    "waas"
]

# used to try to strip service name prefix off of new module names to find a matching old module
# if an entry is missing here it will not properly match resources from that new service with
# modules from the old service
SERVICES_IMPLEMENTED_IN_NEW_MODULES = [
    'compute',
    'loadbalancer',
    'load_balancer',
    'blockstorage',
    'network',
    'identity',
    'budget',
    'container_engine',
    'object_storage',
    'healthchecks',
    'file_storage',
    'audit'
]

########################################################################################
# USER TO UPDATE
########################################################################################
# e.g. "~/ansible-cloud-module/ansible/lib/ansible/modules/cloud/oracle/"
OLD_REPO_MODULES_PATH = ""
# e.g. "~/ansible_collections_oci/ansible_collections/oracle/oci/plugins/modules/"
NEW_REPO_MODULES_PATH = ""

# if either of these are specified it will limit backwards compatibility checking to either a list of modules or only modules matching a prefix:
NEW_MODULES_TO_PROCESS = []

# example: "oci_load_balancer"
NEW_MODULES_TO_PROCESS_PREFIX = "oci_loadbal" #"oci_load_balancer" # oci_identity_compartment_facts" #oci_load_balancer"


def strip_extension(s):
    return os.path.splitext(s)[0]

def add_options_based_on_doc_fragments(doc, options, doc_fragment_name, options_to_create, param_type="str"):
    if 'extends_documentation_fragment' in doc and doc_fragment_name in doc['extends_documentation_fragment']:
        for option in options_to_create:
            options[option] = {
                "type": param_type
            }


def compare_modules(old_module_path, new_module_path):
    old_module_name = strip_extension(ntpath.basename(old_module_path))
    new_module_name = strip_extension(ntpath.basename(new_module_path))

    raw_doc_old_module = get_raw_section_from_module_file(old_module_path, "DOCUMENTATION")
    raw_doc_new_module = get_raw_section_from_module_file(new_module_path, "DOCUMENTATION")

    raw_return_old_module = get_raw_section_from_module_file(old_module_path, "RETURN")
    raw_return_new_module = get_raw_section_from_module_file(new_module_path, "RETURN")

    doc_old_module = yaml.load(raw_doc_old_module, Loader=Loader)
    doc_new_module = yaml.load(raw_doc_new_module, Loader=Loader)

    return_old_module = yaml.load(raw_return_old_module, Loader=Loader)
    return_new_module = yaml.load(raw_return_new_module, Loader=Loader)

    options_old_module = doc_old_module.get("options", {})
    options_new_module = doc_new_module.get("options", {})

    backwards_compatiblity_issues = []

    # there are some very common options that are handled through extends doc fragment
    add_options_based_on_doc_fragments(doc_old_module, options_old_module, "oracle_tags", ["defined_tags", "freeform_tags"], param_type="dict")
    add_options_based_on_doc_fragments(doc_new_module, options_new_module, "oracle_tags", ["defined_tags", "freeform_tags"], param_type="dict")

    add_options_based_on_doc_fragments(doc_old_module, options_old_module, "oracle.oci.oracle_display_name_option", ["display_name"])
    add_options_based_on_doc_fragments(doc_new_module, options_new_module, "oracle.oci.oracle_display_name_option", ["display_name"])

    add_options_based_on_doc_fragments(doc_old_module, options_old_module, "oracle_display_name_option", ["display_name"])
    add_options_based_on_doc_fragments(doc_new_module, options_new_module, "oracle_display_name_option", ["display_name"])

    add_options_based_on_doc_fragments(doc_old_module, options_old_module, "oracle_name_option", ["name"])
    add_options_based_on_doc_fragments(doc_new_module, options_new_module, "oracle_name_option", ["name"])

    add_options_based_on_doc_fragments(doc_old_module, options_old_module, "oracle.oci.oracle_name_option", ["name"])
    add_options_based_on_doc_fragments(doc_new_module, options_new_module, "oracle.oci.oracle_name_option", ["name"])

    len_options_1 = len(options_old_module)
    len_options_2 = len(options_new_module)

    if len_options_1 != len_options_2:
        backwards_compatiblity_issues.append('\t* Mismatch in options length. {} options: {}, {} options: {}'.format(old_module_name, len_options_1, new_module_name, len_options_2))

    # find options that are in options 1 and not options 2
    old_module_only = [k for k,v in six.iteritems(options_old_module) if k not in options_new_module]

    # find options that are in options 2 and not in options 1
    new_module_only = [k for k,v in six.iteritems(options_new_module) if k not in options_old_module]

    is_back_compat = True

    if list(return_old_module)[0] != list(return_new_module)[0]:
        is_back_compat = False
        backwards_compatiblity_issues.append('\t* Return field mismatch. Old module return field: {}, new module return field: {}'.format(list(return_old_module)[0], list(return_new_module)[0]))

    for k,v in six.iteritems(options_new_module):
        if k in old_module_only or k in new_module_only:
            continue
        
        # options that are in both modules, check that type and aliases match
        old_module_option = options_old_module.get(k)
        new_module_option = v

        old_module_option_type = old_module_option.get("type", None)
        new_module_option_type = new_module_option.get("type", None)

        ignore = False

        # seems to be a common issue where we dont assign types to complex params in old modules so ignore this
        if old_module_option_type is None and old_module_option.get("suboptions"):
            ignore = True

        if not old_module_option_type:
            old_module_option_type = "str"

        if not new_module_option_type:
            new_module_option_type = "str"

        if not ignore and old_module_option_type != new_module_option_type:
            backwards_compatiblity_issues.append('\t* Type mismatch in param: {}. Old module type: {}, new module type: {}'.format(k, old_module_option_type, new_module_option_type))
            is_back_compat = False

        old_module_option_aliases = old_module_option.get("aliases",[])
        new_module_option_aliases = new_module_option.get("aliases", [])
        if old_module_option_aliases != new_module_option_aliases:
            backwards_compatiblity_issues.append('\t* Alias mismatch in param: {}. Old module aliases: {}, new module aliases: {}'.format(k, ','.join(old_module_option_aliases), ','.join(new_module_option_aliases)))
            is_back_compat = False

    if old_module_only:
        is_back_compat = False
        backwards_compatiblity_issues.append("\t* Options only present in old module {}: \n\t\t - {}".format(old_module_name, '\n\t\t - '.join(old_module_only)))

    if new_module_only:
        backwards_compatiblity_issues.append("\t* Options only present in new module {}: \n\t\t - {}".format(old_module_name, '\n\t\t - '.join(new_module_only)))

    if backwards_compatiblity_issues:
        print('{} ({})'.format(old_module_name, new_module_name))
        for issue in backwards_compatiblity_issues:
            print(issue)
        print("")

    return is_back_compat


def get_raw_documentation_content_from_module_file_content(module_path):
    return get_raw_section_from_module_file(module_path, "DOCUMENTATION")


def get_raw_section_from_module_file(module_path, section):
    with open(module_path, 'r') as f:
        lines = f.readlines()
        doc_content_lines = []
        inside_doc_string = False
        for line in lines:
            if '{} = """'.format(section) in line:
                inside_doc_string = True
                continue
            
            if '"""' in line:
                inside_doc_string = False
            
            if inside_doc_string:
                doc_content_lines.append(line.replace("\\\\", "\\"))
        
        return ''.join(doc_content_lines)

def strip_prefixes_safe(s, prefixes):
    for prefix in prefixes:
        if s.startswith(prefix):
            return s[len(prefix):]
    
    return s


def is_old_module_from_service_not_yet_implemented(old_repo_modules_path, old_module_name):
    with open(os.path.join(old_repo_modules_path, old_module_name), 'r') as f:
        content = f.read()
    
    for service in SERVICES_NOT_YET_IMPLEMENTED_IN_NEW_MODULES:
        if 'from oci.{}'.format(service) in content:
            return True
    
    return False


def get_old_new_module_pairs(old_repo_modules_path, new_repo_modules_path):
    files_to_exclude = ["__init__.py"]

    old_module_names = [f for f in os.listdir(old_repo_modules_path) if os.path.isfile(os.path.join(old_repo_modules_path, f)) and f not in files_to_exclude]
    new_module_names = [f for f in os.listdir(new_repo_modules_path) if os.path.isfile(os.path.join(new_repo_modules_path, f)) and f not in files_to_exclude]

    unmatched_old_modules = []
    unmatched_new_modules = []

    pairs = []
    # find old module matches for new modules
    for new_module_name in new_module_names:
        found_match_for_new_module = False
        new_model_name_no_oci_prefix = strip_prefixes_safe(new_module_name, ['oci_'])
        new_model_name_no_service_prefix = strip_prefixes_safe(new_model_name_no_oci_prefix, [service_name + "_" for service_name in SERVICES_IMPLEMENTED_IN_NEW_MODULES])

        for old_module_name in old_module_names:
            old_model_name_no_oci_prefix = strip_prefixes_safe(old_module_name, ['oci_'])
            old_model_name_no_service_prefix = strip_prefixes_safe(old_model_name_no_oci_prefix, [service_name + "_" for service_name in SERVICES_IMPLEMENTED_IN_NEW_MODULES])
            if old_model_name_no_oci_prefix == new_model_name_no_oci_prefix or old_model_name_no_oci_prefix == new_model_name_no_service_prefix or old_model_name_no_service_prefix == new_model_name_no_service_prefix:
                pairs.append((old_module_name, new_module_name))
                found_match_for_new_module = True

        if not found_match_for_new_module:
            unmatched_new_modules.append(new_module_name)

    # for info purposes, see if we can find new modules for all old modules
    for old_module_name in old_module_names:
        found_match_for_old_module = False
        old_model_name_no_oci_prefix = strip_prefixes_safe(old_module_name, ['oci_'])

        for new_module_name in new_module_names:
            new_model_name_no_oci_prefix = strip_prefixes_safe(new_module_name, ['oci_'])
            new_model_name_no_service_prefix = strip_prefixes_safe(new_model_name_no_oci_prefix, [service_name + "_" for service_name in SERVICES_IMPLEMENTED_IN_NEW_MODULES])
            if old_model_name_no_oci_prefix == new_model_name_no_oci_prefix or old_model_name_no_oci_prefix == new_model_name_no_service_prefix:
                found_match_for_old_module = True

        # if its from a service we haven't worked on yet, then no need to report it as match not found
        if not found_match_for_old_module and not is_old_module_from_service_not_yet_implemented(old_repo_modules_path, old_module_name):
            unmatched_old_modules.append(old_module_name)


    full_path_pairs = []
    for pair in pairs:
        full_path_pairs.append(
            (
                os.path.join(old_repo_modules_path, pair[0]),
                os.path.join(new_repo_modules_path, pair[1])
            )
        )

    unmatched_old_modules.sort()
    unmatched_new_modules.sort()

    print(separator)
    print("Module matching between old and new")
    print(separator)
    print("Did not find matches for old modules: \n\t{}".format('\n\t'.join(unmatched_old_modules)))
    print("")
    print("Did not find matches for new modules: \n\t{}".format('\n\t'.join(unmatched_new_modules)))
    print("")

    full_path_pairs.sort(key=lambda p: p[0])

    return full_path_pairs, unmatched_old_modules, unmatched_new_modules


if __name__ == "__main__":
    pairs, unmatched_old_modules, unmatched_new_modules = get_old_new_module_pairs(OLD_REPO_MODULES_PATH, NEW_REPO_MODULES_PATH)

    backwards_incompatible_modules = []
    backwards_compatible_modules = []
    total_modules_processed = 0

    print(separator)
    print("Backwards compatibility for matched modules")
    print(separator)

    for old_module_path, new_module_path in pairs:
        new_module_name = strip_extension(ntpath.basename(new_module_path))
        if NEW_MODULES_TO_PROCESS_PREFIX and not new_module_name.startswith(NEW_MODULES_TO_PROCESS_PREFIX):
            continue

        if NEW_MODULES_TO_PROCESS and new_module_name not in NEW_MODULES_TO_PROCESS:
            continue
        
        total_modules_processed = total_modules_processed + 1

        is_back_compat = compare_modules(old_module_path, new_module_path)
        if not is_back_compat:
            backwards_incompatible_modules.append(new_module_name)
        else:
            backwards_compatible_modules.append(new_module_name)
    
    print("")
    print(separator)
    print("Backwards compatibility summary")
    print(separator)
    print("backwards incompatible modules:\n\t{}".format('\n\t'.join(backwards_incompatible_modules)))

    print("")
    print("backwards compatible modules:\n\t{}".format('\n\t'.join(backwards_compatible_modules)))
    print(separator)
    print("Total modules processed: {}. Back compat: {}. Non-back compat: {}. Unmatched new modules*: {}. Unmatched old modules*: {}".format(
        total_modules_processed,
        len(backwards_compatible_modules),
        len(backwards_incompatible_modules),
        len(unmatched_new_modules),
        len(unmatched_old_modules),
    ))
    print("** Note module name filter is applied POST matching, so match / unmatched count reflects all modules in folder **")

