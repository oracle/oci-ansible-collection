#!/usr/bin/env python
# coding: utf-8
# Copyright (c) 2019, Oracle and/or its affiliates. All rights reserved.
#
# Usage: python format_generated_descriptions.py "~/dev/SDK/ansible-cloud-module/ansible/lib/ansible/modules/cloud/oracle/oci_*.py"
#
import os
import glob
import sys
import yaml

import textwrap

if len(sys.argv) < 2:
    sys.exit("Usage Error: Must pass 1 argument containing pattern of files to format")

CONFIG_KEY_MODULE_WHITELIST = "moduleWhitelist"

ALL_MODULES_PATTERN = os.path.expanduser(sys.argv[1])
MODULE_WHITELIST = []
if len(sys.argv) > 2:
    whitelist_file = os.path.expanduser(sys.argv[2])
    with open(whitelist_file, "r") as f:
        MODULE_WHITELIST = yaml.safe_load(f)[CONFIG_KEY_MODULE_WHITELIST]


MAX_LINE_LENGTH = 160
DESCRIPTION_INDENT = 4

SECTION_HEADERS = ['DOCUMENTATION = """', 'RETURN = """']
SECTION_ENDING = '"""'


def get_all_files():
    all_module_files = glob.glob(ALL_MODULES_PATTERN)

    all_module_files = [
        module_file
        for module_file in all_module_files
        if (
            len(MODULE_WHITELIST) == 0
            or os.path.splitext(os.path.basename(module_file))[0] in MODULE_WHITELIST
        )
    ]

    if len(all_module_files) == 0:
        print(
            "No modules found matching pattern: {} and in whitelist: {}".format(
                ALL_MODULES_PATTERN, str(MODULE_WHITELIST)
            )
        )
        sys.exit(0)

    return all_module_files


def reformat_file(file_path):
    print("Re-formatting file: {}".format(file_path))

    with open(file_path, "r") as f:
        content = f.read().splitlines()

    formatted_lines = []
    in_block_description = False
    last_indent = ""
    in_relevant_section = False
    for line in content:
        # only re-format certain sections of the file
        if line in SECTION_HEADERS:
            in_relevant_section = True
        elif line == SECTION_ENDING:
            in_relevant_section = False

        if not in_relevant_section:
            formatted_lines.append(line)
            continue

        generated_one_line_description_prefix = "description: "
        generated_empty_description = generated_one_line_description_prefix + '""'
        yaml_list_item_prefix = "- "
        line_indent = len(line) - len(line.lstrip())
        if (
            line.strip() != generated_empty_description
            and line.strip().startswith(generated_one_line_description_prefix)
            and len(line.strip()) > len(generated_one_line_description_prefix)
        ):
            # take descriptions of the format:
            #   description: This is a long one line description with all newlines removed
            # and word wrap them to look like:
            #   description:
            #       - This is a long one line description with all
            #         newlines removed
            line = line.strip()
            description_item_prefix = "- "
            initial_indent = (
                " " * (line_indent + DESCRIPTION_INDENT) + description_item_prefix
            )
            subsequent_indent = " " * (
                line_indent + DESCRIPTION_INDENT + len(description_item_prefix)
            )
            wrapper = textwrap.TextWrapper(
                initial_indent=initial_indent,
                subsequent_indent=subsequent_indent,
                width=MAX_LINE_LENGTH,
            )

            line = remove_prefix(line, generated_one_line_description_prefix)
            formatted_description = wrapper.wrap(line)
            formatted_lines.append(" " * line_indent + "description:")
            formatted_lines.extend(formatted_description)
        elif in_block_description or line.strip().startswith(yaml_list_item_prefix):
            # this section formats all text that is in a bulleted collection (-)
            #
            # for example
            #   description:
            #       - This is a long one line description with all newlines removed
            # and word wrap them to look like:
            #   description:
            #       - This is a long one line description with all
            #         newlines removed
            #
            # it preserves newlines from the existing text as shown in this example:
            #
            #   description:
            #       - This is a big block of text that already contains
            #         some newlines such that most lines are formatted correctly but one of them is
            #         too long.
            #   description:
            #       - This is a big block of text that already contains
            #         some newlines such that most lines are formatted
            #         correctly but one of them is
            #         too long.

            # we are breaking out of a - item
            if (
                in_block_description
                and not line.strip().startswith(yaml_list_item_prefix)
                and line_indent < last_indent
            ):
                in_block_description = False
                formatted_lines.append(line)
                last_indent = line_indent
                continue

            in_block_description = True

            line = line.strip()
            description_item_prefix = "- "
            initial_indent = " " * line_indent
            if line.strip().startswith(yaml_list_item_prefix):
                line_indent = line_indent + len(description_item_prefix)

            subsequent_indent = " " * line_indent
            wrapper = textwrap.TextWrapper(
                initial_indent=initial_indent,
                subsequent_indent=subsequent_indent,
                width=MAX_LINE_LENGTH,
            )

            formatted_description = wrapper.wrap(line)
            formatted_lines.extend(formatted_description)
        else:
            in_block_description = False
            formatted_lines.append(line)

        last_indent = line_indent

    formatted_content = "\n".join(formatted_lines) + "\n"

    with open(file_path, "w") as f:
        f.write(formatted_content)


def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix) :]
    return text


def main():
    all_module_files = get_all_files()
    for path in all_module_files:
        reformat_file(path)


if __name__ == "__main__":
    main()
