import os
import argparse
import subprocess
import sys
import math
import json
import shutil
import yaml

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

import xml.etree.ElementTree as ET

ns = {"ns": "http://maven.apache.org/POM/4.0.0"}

# allow default namespace for output, dont print ns0: prefixes everywhere
ET.register_namespace('', "http://maven.apache.org/POM/4.0.0")

PYTHON_SDK_COPY_FEATURES_CONFIG_FILE_RELATIVE_PATH = 'python-sdk-copy-features-config.yaml'

# there may be services that don't support yet that break generation
# so this is a way to explicitly skip including those modules
# The blacklist entry can be any substring of the `module` element
# in the python-sdk pom.xml
MODULE_BLACKLIST = []

# there was no use case for this that we needed to distinguish
# between feature ids and enabled groups so we can just keep one list
ENABLED_GROUPS_AND_FEATURE_IDS_TO_BLACKLIST = []

# explicitly override the spec version from the python-sdk if we want
# a different version for ansible
SPEC_VERSION_OVERRIDES = {}

ALLOW_WORK_REQUEST_SERVICE = False

PYTHON_SDK_POMS_RELATIVE_PATH = 'poms/'
COLLECTIONS_REPO_POMS_RELATIVE_PATH = 'poms/'

PYTHON_SDK_CODEGEN_CONFIG_RELATIVE_PATH = 'codegenConfig/'
COLLECTIONS_REPO_CODEGEN_CONFIG_RELATIVE_PATH = 'codegenConfig/'

COLLECTIONS_REPO_FEATURE_IDS_RELATIVE_PATH = os.path.join(COLLECTIONS_REPO_CODEGEN_CONFIG_RELATIVE_PATH, 'featureIds')
COLLECTIONS_REPO_ENABLED_GROUPS_RELATIVE_PATH = os.path.join(COLLECTIONS_REPO_CODEGEN_CONFIG_RELATIVE_PATH, 'enabledGroups')

SPEC_NAME_TO_TAGS = {
    "core": {
        "blockstorage",
        "compute",
        "compute_management",
        "network"
    }
}

MAVEN_EXEC_PLUGIN_TEMPLATE = """
<plugin>
    <artifactId>exec-maven-plugin</artifactId>
    <groupId>org.codehaus.mojo</groupId>
    <version>1.6.0</version>
    <executions>
        <execution>
        <id>ansible-modules-{service_name}-clean-generated-modules</id>
        <phase>clean</phase>
        <goals>
            <goal>exec</goal>
        </goals>
        <configuration>
            <executable>${{project-root-dir}}/scripts/clean_generated_modules.py</executable>
            <arguments>
            <argument>${{modules-output-directory}}/oci_{service_name}*.py</argument>
            </arguments>
        </configuration>
        </execution>
        <execution>
        <id>ansible-modules-{service_name}-format-descriptions</id>
        <phase>compile</phase>
        <goals>
            <goal>exec</goal>
        </goals>
        <configuration>
            <executable>${{project-root-dir}}/scripts/format_generated_descriptions.py</executable>
            <arguments>
            <argument>${{modules-output-directory}}/oci_{service_name}*.py</argument>
            <argument>${{module-whitelist-file}}</argument>
            </arguments>
        </configuration>
        </execution>
        <execution>
        <id>ansible-modules-{service_name}-format-code</id>
        <phase>package</phase>
        <goals>
            <goal>exec</goal>
        </goals>
        <configuration>
            <executable>${{project-root-dir}}/scripts/run-black</executable>
            <arguments>
            <argument>${{modules-output-directory}}/oci_{service_name}*.py</argument>
            </arguments>
        </configuration>
        </execution>
    </executions>
</plugin>
"""

MAVEN_CLEAN_PLUGIN_TEMPLATE = """
<plugin>
    <artifactId>maven-clean-plugin</artifactId>
    <version>3.0.0</version>
    <configuration>
        <filesets>
        <fileset>
            <directory>${{test-output-directory}}</directory>
            <includes>
            <include>oci_generated_{service_name}*</include>
            <include>oci_generated_{service_name}*/tasks/*</include>
            <include>oci_generated_{service_name}*/tasks</include>
            <include>oci_generated_{service_name}*/meta/*</include>
            <include>oci_generated_{service_name}*/meta</include>
            <include>oci_generated_{service_name}*/vars</include>
            </includes>
            <excludes>
            <include>oci_generated_{service_name}*/tasks/main.yaml</include>
            <include>oci_generated_{service_name}*/tasks/*_setup.yaml</include>
            <include>oci_generated_{service_name}*/tasks/*_teardown.yaml</include>
            <include>oci_generated_{service_name}*/vars/main.yaml</include>
            </excludes>
        </fileset>
        </filesets>
    </configuration>
</plugin>
"""


class CommentedTreeBuilder(ET.TreeBuilder):
    def __init__(self, *args, **kwargs):
        super(CommentedTreeBuilder, self).__init__(*args, **kwargs)

    def comment(self, data):
        self.start(ET.Comment, {})
        self.data(data)
        self.end(ET.Comment)


def parse_pom(pom_file_path):
    return ET.parse(pom_file_path, parser=ET.XMLParser(target=CommentedTreeBuilder()))

def write_xml(file_name, pom):
    indent(pom.getroot())
    if not os.path.exists(os.path.dirname(file_name)):
        os.makedirs(os.path.dirname(file_name))

    with open(file_name, 'w'):
        pom.write(file_name, encoding="UTF-8", xml_declaration=True)

def indent(elem, level=0):
    indent_str = "  "
    i = "\n" + level * indent_str
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + indent_str
        for e in elem:
            indent(e, level + 1)
            if not e.tail or not e.tail.strip():
                e.tail = i + indent_str
        if not e.tail or not e.tail.strip():
            e.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


def replace_element_text(pom, xpath, text):
    results = pom.findall(xpath, ns)

    for result in results:
        result.text = text


def add_child_element_from_string(pom, parent_xpath, s):
    return add_child_element(pom, parent_xpath, ET.fromstring(s))


def add_child_element(pom, parent_xpath, element):
    results = pom.findall(parent_xpath, ns)

    for result in results:
        result.append(element)

def remove_child_element(pom, parent_xpath, child_xpath):
    parent_results = pom.findall(parent_xpath, ns)
    children = pom.findall(child_xpath, ns)

    if len(parent_results) > 1:
        raise RuntimeError("Cant remove from multiple parents")
    
    parent = parent_results[0]
    for child in children:
        parent.remove(child)


def module_name_is_blacklisted(module_name):
    return len([module_name for blacklist_entry in MODULE_BLACKLIST if blacklist_entry in module_name]) > 0


def process_feature_id_files_against_blacklist(feature_id_files_directory, blacklist):
    for name in os.listdir(feature_id_files_directory):
        full_path = os.path.join(feature_id_files_directory, name)
        if os.path.isfile(full_path):
            with open(full_path, 'r+') as feature_id_file:
                content = feature_id_file.read()

                # avoid yaml parsing every file if it doesnt contain a blacklisted feature id
                need_to_parse = False
                for blacklisted_enabled_group in blacklist:
                    if blacklisted_enabled_group in content:
                        need_to_parse = True
                        break

                if need_to_parse:
                    doc = yaml.safe_load(content)
                    whitelist = doc["whitelisted"]

                    need_to_overwrite = False
                    for blacklisted_enabled_group in blacklist:
                        if blacklisted_enabled_group in whitelist:
                            whitelist.remove(blacklisted_enabled_group)
                            need_to_overwrite = True
                    
                    if need_to_overwrite:
                        print("Needed to overwrite: {}".format(full_path))
                        feature_id_file.seek(0)
                        yaml.dump(doc, feature_id_file)
                        feature_id_file.truncate()


def process_enabled_groups_files_against_blacklist(enabled_groups_files_directory, blacklist):
    for name in os.listdir(enabled_groups_files_directory):
        full_path = os.path.join(enabled_groups_files_directory, name)
        if os.path.isfile(full_path):
            with open(full_path, 'r+') as enabled_groups_file:
                content_lines = enabled_groups_file.readlines()
                need_to_overwrite = False
                new_lines = []

                for line in content_lines:
                    skip_line = False
                    for blacklisted_enabled_group in blacklist:
                        if line.strip() == blacklisted_enabled_group:
                            skip_line = True
                            break
                    
                    if skip_line:
                        need_to_overwrite = True
                    else:
                        new_lines.append(line)

                if need_to_overwrite:
                    print("Needed to overwrite: {}".format(full_path))
                    enabled_groups_file.seek(0)
                    enabled_groups_file.write(''.join(new_lines))
                    enabled_groups_file.truncate()


def main(python_sdk_dir, ansible_collections_repo_dir, copy_codegen_config_enabled):
    print("Copying and processing poms...")
    pom_paths = []
    poms_dir = os.path.join(python_sdk_dir, PYTHON_SDK_POMS_RELATIVE_PATH)
    for root, dirs, files in os.walk(poms_dir):
        for f in files:
            pom_paths.append(os.path.join(root, f))

    for pom_path in pom_paths:
        pom = parse_pom(pom_file_path=pom_path)

        additional_properties_xpath = ".//ns:plugin[ns:artifactId='bmc-sdk-swagger-maven-plugin']/ns:executions/ns:execution//ns:additionalProperties"
        configuration_xpath = ".//ns:plugin[ns:artifactId='bmc-sdk-swagger-maven-plugin']/ns:executions/ns:execution/ns:configuration"
        plugins_xpath = ".//ns:plugins"
        spec_name_xpath = ".//ns:plugin[ns:artifactId='bmc-sdk-swagger-maven-plugin']//ns:specName"

        spec_name = pom.findall(spec_name_xpath, ns)[0].text

        add_child_element_from_string(pom, configuration_xpath, "<testOutputDir>${test-output-directory}</testOutputDir>")

        replace_element_text(pom, ".//ns:plugin[ns:artifactId='bmc-sdk-swagger-maven-plugin']/ns:executions/ns:execution/ns:configuration/ns:outputDir", "${output-directory}")

        replace_element_text(pom, "./ns:artifactId", "ansible-modules-{spec_name}-codegen".format(spec_name=spec_name))

        add_child_element_from_string(pom, additional_properties_xpath, "<moduleWhitelistPath>${module-whitelist-file}</moduleWhitelistPath>")
        add_child_element_from_string(pom, additional_properties_xpath, "<moduleRenameConfigPath>${module-rename-file}</moduleRenameConfigPath>")
        add_child_element_from_string(pom, additional_properties_xpath, "<supplementalExamplesConfigPath>${supplemental-examples-file}</supplementalExamplesConfigPath>")

        remove_child_element(pom, ".//ns:plugin[ns:artifactId='bmc-sdk-swagger-maven-plugin']/ns:executions/ns:execution//ns:configuration", ".//ns:plugin[ns:artifactId='bmc-sdk-swagger-maven-plugin']/ns:executions/ns:execution//ns:configuration/ns:featureIdConfigFile")

        remove_child_element(pom, ".//ns:plugins", ".//ns:plugin[ns:artifactId='maven-clean-plugin']")

        remove_child_element(pom, "./ns:properties", "./ns:properties/ns:spec-temp-dir")
        remove_child_element(pom, "./ns:properties", "./ns:properties/ns:preprocessed-temp-dir")
        remove_child_element(pom, "./ns:properties", "./ns:properties/ns:preferred-temp-dir")
        remove_child_element(pom, "./ns:properties", "./ns:properties/ns:enabled-groups-dir")
        remove_child_element(pom, "./ns:properties", "./ns:properties/ns:feature-id-file")
        remove_child_element(pom, "./ns:properties", "./ns:properties/ns:feature-id-dir")

        if spec_name in SPEC_NAME_TO_TAGS:
            for tag in SPEC_NAME_TO_TAGS[spec_name]:
                add_child_element_from_string(pom, plugins_xpath, MAVEN_EXEC_PLUGIN_TEMPLATE.format(service_name=tag))
                add_child_element_from_string(pom, plugins_xpath, MAVEN_CLEAN_PLUGIN_TEMPLATE.format(service_name=tag))    
        else:
            add_child_element_from_string(pom, plugins_xpath, MAVEN_EXEC_PLUGIN_TEMPLATE.format(service_name=spec_name))
            add_child_element_from_string(pom, plugins_xpath, MAVEN_CLEAN_PLUGIN_TEMPLATE.format(service_name=spec_name))
        
        if spec_name in SPEC_VERSION_OVERRIDES:
            replace_element_text(pom, ".//ns:dependencyManagement//ns:version", SPEC_VERSION_OVERRIDES.get(spec_name))

        if not ALLOW_WORK_REQUEST_SERVICE:
            remove_child_element(pom, additional_properties_xpath, ".//ns:specUsesWorkRequestService")

        # replace new dex-get-spec-artifact-plugin with the old plugin that downloads directly from artifactory
        replace_element_text(pom, ".//ns:plugin[ns:artifactId='dex-get-spec-artifact-plugin']/ns:version", "2.10")
        replace_element_text(pom, ".//ns:plugin[ns:artifactId='dex-get-spec-artifact-plugin']/ns:groupId", "org.apache.maven.plugins")
        replace_element_text(pom, ".//ns:plugin[ns:artifactId='dex-get-spec-artifact-plugin']/ns:artifactId", "maven-dependency-plugin")

        if spec_name == "audit":
            replace_element_text(pom, ".//ns:hemlock-spec-spec-file", "hemlock-api-20160918.yaml")

        # write output
        pom_subfolder = os.path.basename(os.path.dirname(pom_path))
        output_file = os.path.join(ansible_collections_repo_dir, COLLECTIONS_REPO_POMS_RELATIVE_PATH, pom_subfolder, 'pom.xml')
        write_xml(output_file, pom)

    # copy modules from python sdk pom and insert into collections repo pom applying service blacklist
    python_sdk_root_pom = parse_pom(os.path.join(python_sdk_dir, 'pom.xml'))
    collections_root_pom = parse_pom(os.path.join(ansible_collections_repo_dir, 'pom.xml'))

    python_sdk_modules = python_sdk_root_pom.findall(".//ns:module", ns)
    modules_to_add = [module for module in python_sdk_modules if not module_name_is_blacklisted(module.text)]

    remove_child_element(collections_root_pom, "./ns:modules", "./ns:modules/ns:module")
    for module in modules_to_add:
        add_child_element(collections_root_pom, ".//ns:modules", module)

    output_file = os.path.join(ansible_collections_repo_dir, 'pom.xml')
    write_xml(output_file, collections_root_pom)

    if copy_codegen_config_enabled:
        print("Copying codegenConfig dirs...")

        # copy all of codegenConfig from python-sdk to ansible
        collections_repo_codegen_config_dir = os.path.join(ansible_collections_repo_dir, COLLECTIONS_REPO_CODEGEN_CONFIG_RELATIVE_PATH)
        shutil.rmtree(collections_repo_codegen_config_dir)
        shutil.copytree(
            os.path.join(python_sdk_dir, PYTHON_SDK_CODEGEN_CONFIG_RELATIVE_PATH),
            collections_repo_codegen_config_dir
        )

        print("Processing featureId blacklist...")
        process_feature_id_files_against_blacklist(COLLECTIONS_REPO_FEATURE_IDS_RELATIVE_PATH, ENABLED_GROUPS_AND_FEATURE_IDS_TO_BLACKLIST)
        print("Processing enabledGroups blacklist...")
        process_enabled_groups_files_against_blacklist(COLLECTIONS_REPO_ENABLED_GROUPS_RELATIVE_PATH, ENABLED_GROUPS_AND_FEATURE_IDS_TO_BLACKLIST)
    else:
        print("Skipped copying codegenConfig dir")


def load_global_config(ansible_collections_repo_dir):
    global MODULE_BLACKLIST;
    global ENABLED_GROUPS_AND_FEATURE_IDS_TO_BLACKLIST;
    global SPEC_VERSION_OVERRIDES;

    # read config
    script_config_path = os.path.join(args.ansible_collections_repo_dir, PYTHON_SDK_COPY_FEATURES_CONFIG_FILE_RELATIVE_PATH)
    with open(script_config_path, 'r') as f:
        config = yaml.load(f.read())

    MODULE_BLACKLIST = config["python_sdk_pom_modules_blacklist"]
    ENABLED_GROUPS_AND_FEATURE_IDS_TO_BLACKLIST = config["python_sdk_features_blacklist"]
    SPEC_VERSION_OVERRIDES =config["python_sdk_spec_version_overrides"]


if __name__== "__main__":
    parser = argparse.ArgumentParser(description='Run integration tests for oci ansible collection.')
    parser.add_argument('--python-sdk-dir', required=True, help='Path to a local copy of the Python SDK to source the poms from')
    parser.add_argument('--ansible-collections-repo-dir', required=True, help='Path to a local copy of the collections repo to add the poms to')
    parser.add_argument('--copy-codegen-config-enabled', default=False, action='store_true', help='Whether or not to ')

    args = parser.parse_args()

    load_global_config(args.ansible_collections_repo_dir)

    main(python_sdk_dir=args.python_sdk_dir, ansible_collections_repo_dir=args.ansible_collections_repo_dir, copy_codegen_config_enabled=args.copy_codegen_config_enabled)


