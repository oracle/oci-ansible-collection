#!/usr/bin/env python

# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.


from __future__ import absolute_import, division, print_function

import argparse
import shutil
import sys
import os
import subprocess
import tempfile
import platform
from urllib.request import urlopen


class CollectionInstallerException(Exception):
    pass


class OciAnsibleCollectionInstaller:
    MIN_PYTHON_VERSION_MAJOR = 3
    MIN_PYTHON_VERSION_MINOR = 6
    ORACLE_COLLECTION_NAMESPACE = "oracle.oci"
    DEFAULT_VENV_DIR = os.path.expanduser(os.path.join("~", "venv"))
    DEFAULT_VENV_NAME = "oci-ansible-collection"

    DEPENDENCIES = ["oci", "ansible"]
    GET_PIP_DOWNLOAD_URL = "https://bootstrap.pypa.io/get-pip.py"

    def __init__(
        self,
        dry_run=False,
        interactive=False,
        virtual_env_directory=None,
        virtual_env_name=None,
        ansible_version=None,
        oci_ansible_collection_path=None,
        oci_ansible_collection_version=None,
        upgrade_pip=True,
        verbose=False,
    ):
        self.dry_run = dry_run
        self.upgrade_pip = upgrade_pip or False
        self.interactive = interactive or False
        self.virtual_env_directory = virtual_env_directory or self.DEFAULT_VENV_DIR
        self.virtual_env_name = virtual_env_name or self.DEFAULT_VENV_NAME
        self.ansible_version = ansible_version
        self.oci_ansible_collection_path = oci_ansible_collection_path
        self.oci_ansible_collection_version = oci_ansible_collection_version
        self.verbose = verbose or False

        self.python_path = None  # value is set to venv python path if provided

    def _get_collection_name(self):
        name = self.ORACLE_COLLECTION_NAMESPACE
        if self.oci_ansible_collection_version:
            name = name + ":==" + self.oci_ansible_collection_version
        return name

    def _debug(self, msg):
        if self.verbose:
            print("-- " + msg)

    def _log(self, msg):
        print("-- " + msg)

    def _fail(self, msg):
        print("-- " + msg)
        sys.exit(1)

    def _get_linux_distribution_id_like(self):
        # An example of a line in /etc/os-release is ID_LIKE=ubuntu
        # An example of a line in /etc/os-release is ID=debian
        # See ID, ID_LIKE on https://www.freedesktop.org/software/systemd/man/os-release.html

        id_value = id_like_value = None
        try:
            with open("/etc/os-release") as lines:
                for line in lines:
                    if "=" in line:
                        key, value = line.split("=", 1)
                        if key.lower() == "id_like":
                            id_like_value = value.lower()
                        if key.lower() == "id":
                            id_value = value.lower()
                return id_value, id_like_value
        except Exception:
            return id_value, id_like_value

    def _is_ubuntu_or_debian(self):
        (
            linux_distribution_id,
            linux_distribution_id_like,
        ) = self.get_linux_distribution_id_like()
        return (
            linux_distribution_id_like
            and any(x in linux_distribution_id_like for x in ["ubuntu", "debian"])
        ) or (
            linux_distribution_id
            and any(x in linux_distribution_id for x in ["ubuntu", "debian"])
        )

    # def get_ubuntu_version(self):
    #     try:
    #         with open("/etc/os-release") as f:
    #             d = {}
    #             for line in f:
    #                 k, v = line.rstrip().split("=")
    #                 d[k.lower()] = v.strip('"')
    #         return d["version_id"] if d["name"] == "Ubuntu" else None
    #     except Exception as e:
    #         return None

    def _install_python3_venv(self):
        cmd = ["sudo", "apt-get", "update"]
        self._exec(cmd)

        self._debug("Installing python3-venv...")
        cmd = ["sudo", "apt-get", "install", "python3-venv", "-y"]
        self._exec(cmd)

    def _exec(self, cmd):
        if not self.dry_run:
            try:
                subprocess.check_call(cmd)
                self._debug("Executing command: " + str(cmd))
            except Exception as e:
                self._fail("Error while running command {0} {1}".format(cmd, str(e)))

    def _exec_output(self, cmd):
        if not self.dry_run:
            try:
                return subprocess.check_output(cmd)
            except Exception as e:
                self._fail("Error while running command {0} {1}".format(cmd, str(e)))

    def _get_pip_path(self):
        base_path = self.python_path
        pip2 = os.path.join(base_path, "bin/pip")
        pip3 = os.path.join(base_path, "bin/pip3")
        if os.path.exists(pip3):
            return pip3

        self._debug("Using pip2 {} for installing dependencies".format(pip2))
        return pip2

    def _get_ansible_galaxy_path(self):
        return os.path.join(self.python_path, "bin/ansible-galaxy")

    def verify_os(self):
        if (
            sys.platform == "win32"
            or sys.platform == "win64"
            or "Windows" in platform.system()
        ):
            self._fail("Not supported for windows based OS")

    def verify_python_version(self):
        self._debug("Verifying Python version.")
        version = sys.version_info
        if not (
            version.major >= self.MIN_PYTHON_VERSION_MAJOR
            and version.minor >= self.MIN_PYTHON_VERSION_MINOR
        ):
            raise CollectionInstallerException(
                "oci-ansible-collection requires Python version >= {}.{}".format(
                    self.MIN_PYTHON_VERSION_MAJOR, self.MIN_PYTHON_VERSION_MINOR
                )
            )
        self._debug(
            "Python version {0}.{1}.{2} okay.".format(
                version.major, version.minor, version.micro
            )
        )

    def setup_venv(self):
        base_path = os.path.join(self.virtual_env_directory, self.virtual_env_name)
        if not os.path.exists(base_path):
            cmd = [sys.executable, "-m", "venv", base_path]
            self._exec(cmd)
            self._debug(
                "Virtual environment {0} created successfully".format(base_path)
            )
        self.python_path = base_path
        self._debug(
            "Using following python environment for package management {}".format(
                self.python_path
            )
        )

    def setup_pip(self):
        pip_path = self._get_pip_path()
        if os.path.exists(pip_path):
            self._debug("pip already installed at {}".format(pip_path))
            if self.upgrade_pip:
                cmd = [pip_path, "install", "--upgrade", "pip", "-q"]
                self._exec(cmd)
                self._debug("upgraded pip")
        else:
            if not self.dry_run:
                self._debug("Installing pip..")
                tmp_dir = tempfile.mkdtemp()
                try:
                    response = urlopen(self.GET_PIP_DOWNLOAD_URL)
                    tmp_file = os.path.join(tmp_dir, "getpip.py")
                    with (tmp_file, "wb"):
                        tmp_file.write(response.read())
                    cmd = [sys.executable, tmp_file]
                    self._exec(cmd)
                    shutil.rmtree(tmp_dir)
                    self._debug("Installed pip")
                except Exception as e:
                    shutil.rmtree(tmp_dir)
                    self._fail("Error while setting up pip " + str(e))

    def install_dependencies(self):
        pip_path = self._get_pip_path()
        self._debug("Using forllowing pip for package management {}".format(pip_path))
        for dep in self.DEPENDENCIES:
            cmd = [pip_path, "install", dep]
            if not self.verbose:
                cmd.append("-q")
            self._debug("Installing {0} dependency ".format(dep))
            self._exec(cmd)

    def install_ansible_collection(self):
        collection_name = self._get_collection_name()
        ansible_galaxy_path = self._get_ansible_galaxy_path()
        cmd = [ansible_galaxy_path, "collection", "install", collection_name]
        if self.oci_ansible_collection_path:
            cmd.extend(["-p", self.oci_ansible_collection_path])
            self._debug(
                "Installing oci-ansible-collection at {0}".format(
                    self.oci_ansible_collection_path
                )
            )

        if self.verbose:
            cmd.append("-vvv")

        self._exec(cmd)
        self._debug("Installed successfully...")

    def post_installation(self):
        if not self.dry_run:
            pip_path = self._get_pip_path()
            packages = self._exec_output([pip_path, "freeze"]).decode().split("\n")
            packages = [p.split("==")[0] for p in packages]

            for dep in self.DEPENDENCIES:
                if dep not in packages:
                    self._debug("Required {} is not installed".format(dep))
                    return
            self._debug("All dependencies installed correctly")

        activate_venv_cmd = "source " + os.path.join(self.python_path, "bin/activate")
        export_collection_path_cmd = (
            "export ANSIBLE_COLLECTIONS_PATHS=${"
            + "ANSIBLE_COLLECTIONS_PATHS"
            + "}:"
            + self.oci_ansible_collection_path
        )

        print(
            "\n==========================COMMANDS====================================\n"
        )
        print(
            "Run the following commands to use the installed oci-ansible-collection\n"
        )
        print(activate_venv_cmd)
        if self.oci_ansible_collection_path:
            print(export_collection_path_cmd)
        print("\n")
        print("ansible-doc oracle.oci.oci_netowrk_vcn")
        print(
            "\n==========================COMMANDS====================================\n"
        )


def main():
    parser = argparse.ArgumentParser(
        description="Installs ansible collection for Oracle Cloud Infrastructure"
    )
    parser.add_argument(
        "--virtual-env-dir",
        help="""Users can use this flag to specify the location of the python virtual environment where
         python dependencies for oci-ansible-collections will be installed""",
    )
    parser.add_argument(
        "--virtual-env-name",
        help="""Users can use this flag to specify the name of the python virtual env name where
         python dependencies for oci-ansible-collections will be installed""",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="""Users can use this flag to enable logs""",
    )
    parser.add_argument(
        "--ansible-version",
        help="""Users can specify particular version of ansible python package they want to install. Ex: >=2.9.
                    To use the latest version dont't set this flag (recommended)""",
    )
    parser.add_argument(
        "--upgrade-pip",
        action="store_true",
        help="""Users can set this flag to upgrade pip present in the virtual environment""",
    )
    parser.add_argument(
        "--oci-ansible-collection-path",
        help="""Users can use this flag to specify the location of collections where oci-ansible-collection will be installed""",
    )
    parser.add_argument(
        "--version",
        help="""Users can use this flag to specify the version of oci-ansible-collection will be installed.
                    To use the latest version don't set any value(recommended)""",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="""Runs the script in dry run mode i.e no network calls and installation of dependecies""",
    )

    args = parser.parse_args()

    installer = OciAnsibleCollectionInstaller(
        dry_run=args.dry_run,
        upgrade_pip=args.upgrade_pip,
        verbose=args.verbose,
        virtual_env_directory=args.virtual_env_dir,
        virtual_env_name=args.virtual_env_name,
        ansible_version=args.ansible_version,
        oci_ansible_collection_path=args.oci_ansible_collection_path,
        oci_ansible_collection_version=args.version,
    )

    installer.verify_python_version()
    installer.verify_os()

    installer.setup_venv()
    installer.setup_pip()
    installer.install_dependencies()
    installer.install_ansible_collection()

    installer.post_installation()


if __name__ == "__main__":
    main()
