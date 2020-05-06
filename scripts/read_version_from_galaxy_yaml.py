# Copyright (c) 2020 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.
import yaml
import os


try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


def read_version_from_galaxy():
    galaxy_yml_file = open("{0}/galaxy.yml".format(os.getcwd()), "r")
    galaxy_yml_file_content = yaml.load(galaxy_yml_file.read(), Loader=Loader)
    version = galaxy_yml_file_content["version"]
    galaxy_yml_file.close()
    return version
