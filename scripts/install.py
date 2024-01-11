#!/usr/bin/env python

# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
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
    DEFAULT_VENV_DIR = os.path.expanduser(os.path.join("~", "lib"))
    DEFAULT_VENV_NAME = "oci-ansible-collection"
    SUPPORTS_UPGRADE = ["oci"]
    DEPENDENCIES = {"oci": None, "ansible": None}
    GET_PIP_DOWNLOAD_URL = "https://bootstrap.pypa.io/get-pip.py"
    LINUX_DISTRIBUTIONS = ["ubuntu", "debian"]

    def __init__(
        self,
        dry_run=False,
        virtual_env_directory=None,
        virtual_env_name=None,
        ansible_version=None,
        oci_ansible_collection_path=None,
        oci_ansible_collection_version=None,
        verbose=False,
        upgrade=False,
    ):
        self.dry_run = dry_run
        self.virtual_env_directory = virtual_env_directory or self.DEFAULT_VENV_DIR
        self.virtual_env_name = virtual_env_name or self.DEFAULT_VENV_NAME

        self.DEPENDENCIES["ansible"] = ansible_version

        self.oci_ansible_collection_path = oci_ansible_collection_path
        self.oci_ansible_collection_version = oci_ansible_collection_version
        self.verbose = verbose or False
        self.upgrade = upgrade

        if self.upgrade and self.oci_ansible_collection_version:
            self._fail(
                "Conflicting arguments provided. Either pass --upgrade or --version, not both"
            )

        self.base_path = None  # path to the venv dir
        self.python_path = None  # path to the venv python

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
        print("-- ERROR: " + msg)
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
        ) = self._get_linux_distribution_id_like()
        return (
            linux_distribution_id_like
            and any(x in linux_distribution_id_like for x in self.LINUX_DISTRIBUTIONS)
        ) or (
            linux_distribution_id
            and any(x in linux_distribution_id for x in self.LINUX_DISTRIBUTIONS)
        )

    def _install_python3_venv(self):
        cmd = ["sudo", "apt-get", "update"]
        self._exec(cmd)

        self._debug("Installing python3-venv...")
        cmd = ["sudo", "apt-get", "install", "python3-venv", "-y"]
        self._exec(cmd)

    def _exec(self, cmd):
        if not self.dry_run:
            try:
                self._debug("Executing command: " + str(" ".join(cmd)))
                subprocess.check_call(cmd, stderr=subprocess.STDOUT)
            except subprocess.CalledProcessError as e:
                self._fail("Error while running command {0} {1}".format(cmd, str(e)))

    def _exec_output(self, cmd):
        if not self.dry_run:
            try:
                self._debug("Executing command: " + str(" ".join(cmd)))
                return subprocess.check_output(cmd, stderr=subprocess.STDOUT)
            except subprocess.CalledProcessError as e:
                if "'pip', '--version'" in str(e):
                    self._debug(str(e))
                    raise ModuleNotFoundError("Pip doesnt exist")
                self._fail("Error while running command {0} {1}".format(cmd, str(e)))

    def _get_ansible_galaxy_path(self):
        return os.path.join(self.base_path, "bin", "ansible-galaxy")

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
        # Since Ubuntu and Debian are having issues with python3 venv (mising ensurepip module), install python3-venv
        if self._is_ubuntu_or_debian():
            self._install_python3_venv()

        base_path = os.path.join(self.virtual_env_directory, self.virtual_env_name)
        if not os.path.exists(base_path):
            cmd = [sys.executable, "-m", "venv", base_path]
            self._exec(cmd)
            self._debug(
                "Virtual environment {0} created successfully".format(base_path)
            )
        self.base_path = base_path
        self.python_path = os.path.join(self.base_path, "bin", "python")

        self._debug(
            "Using following python environment for package management {}".format(
                self.base_path
            )
        )

    def _pip_exists(self):
        try:
            version = self._exec_output([self.python_path, "-m", "pip", "--version"])
            self._debug(version.decode("utf-8"))
            return True
        except Exception as e:
            self._debug(str(e))
            return False

    def setup_pip(self):
        if self._pip_exists():
            self._debug("Pip already exists")
        else:
            if not self.dry_run:
                self._debug("Installing pip..")
                tmp_dir = tempfile.mkdtemp()
                try:
                    response = urlopen(self.GET_PIP_DOWNLOAD_URL)
                    tmp_file = os.path.join(tmp_dir, "getpip.py")
                    f = open(os.path.join(tmp_dir, "getpip.py"), "wb")
                    f.write(response.read())
                    f.close()
                    cmd = [
                        sys.executable if not self.python_path else self.python_path,
                        tmp_file,
                    ]
                    self._exec(cmd)
                    shutil.rmtree(tmp_dir)
                    self._debug("Installed pip")
                except Exception as e:
                    shutil.rmtree(tmp_dir)
                    self._fail("Error while setting up pip " + str(e))

        cmd = [
            self.python_path,
            "-m",
            "pip",
            "install",
            "--upgrade",
            "pip",
        ]
        if self.verbose:
            cmd.append("-q")
        self._debug("Upgrading pip...")
        self._exec(cmd)
        self._debug("upgraded pip..")

    def install_dependencies(self):
        for dep in self.DEPENDENCIES:

            # if upgrade is sepcified we dont check for the version provided
            # and install the latest
            if dep not in self.SUPPORTS_UPGRADE or not self.upgrade:
                if self.DEPENDENCIES.get(dep, None):
                    dep = dep + "==" + self.DEPENDENCIES[dep]

            cmd = [self.python_path, "-m", "pip", "install", dep]
            if self.upgrade and dep in self.SUPPORTS_UPGRADE:
                self._debug(
                    "--upgrade arg specified. Will install the latest version for {}".format(
                        dep
                    )
                )
                cmd.append("-U")
            if not self.verbose:
                cmd.append("-q")
            self._debug("Installing dependency: {0}".format(dep))
            self._exec(cmd)

    def install_ansible_collection(self):
        collection_name = self._get_collection_name()
        cmd = [
            self._get_ansible_galaxy_path(),
            "collection",
            "install",
        ]
        # if upgrade arg is passed or no version is given we will install the latest one
        if self.upgrade or not self.oci_ansible_collection_version:
            self._log("Installing latest version of oci-ansible-collection ....")
            cmd.append(self.ORACLE_COLLECTION_NAMESPACE)
            cmd.append("--force")
        else:
            cmd.append(collection_name)

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
        self._log("Installed oci-ansible-collection successfully...")

    def post_installation(self):
        if not self.dry_run:
            packages = (
                self._exec_output([self.python_path, "-m", "pip", "freeze"])
                .decode()
                .split("\n")
            )
            packages = [p.split("==")[0] for p in packages]

            for dep in self.DEPENDENCIES:
                if dep not in packages:
                    self._debug("Required {} is not installed".format(dep))
                    return
            self._debug("All dependencies installed correctly")

        print(
            "\n-- Run the following command(s) to use the installed oci-ansible-collection"
        )

        activate_venv_cmd = "source " + os.path.join(self.base_path, "bin/activate")
        print(activate_venv_cmd)
        if self.oci_ansible_collection_path:
            export_collection_path_cmd = (
                "export ANSIBLE_COLLECTIONS_PATHS="
                + self.oci_ansible_collection_path
                + ":${"
                + "ANSIBLE_COLLECTIONS_PATHS}"
            )
            print(export_collection_path_cmd)

        print("\n-- Try the following command to start using oci-ansible-collection")
        print("ansible-doc oracle.oci.oci_network_vcn")
        print(
            "\n==========================NEXT STEPS====================================\n"
        )
        print(
            "-- Configure authentication to manage and access Oracle Cloud resources using oci-ansible-collection\n"
        )
        print("""Follow the link to know more about the configuration setup:""")
        print(
            "https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/ansiblegetstarted.htm#configureAuth."
        )


def main():
    parser = argparse.ArgumentParser(
        description="Installs ansible collection for Oracle Cloud Infrastructure"
    )
    parser.add_argument(
        "--virtual-env-dir",
        help="""Users can use this flag to specify the location where the virtual environment is located or should be created
                if not already present. If this path already exists then it will be used else it will be created.

                default value: ~/lib
                """,
    )

    parser.add_argument(
        "--virtual-env-name",
        help="""Users can use this flag to specify the python virtual env name where python dependencies
                for oci-ansible-collection will be installed.
                This virtual env is created in the path sepcified in --virtual-env-dir flag else in the default folder path
                used by --virtual-env-dir flag,

                default value: oci-ansible-collection
                """,
    )

    parser.add_argument(
        "--verbose",
        action="store_true",
        help="""Users can use this flag to enable logs""",
    )

    parser.add_argument(
        "--ansible-version",
        help="""Users can specify particular version of ansible python package they want to install. Ex: 2.9
                To use the latest version dont't set this flag (recommended).
                This flag doesn't support upgrading the version in case user has already installed ansible
                and wants to upgrade to a higher version.

                default value: latest version will be installed
                """,
    )

    parser.add_argument(
        "--oci-ansible-collection-path",
        help="""Users can use this flag to specify the location of collections where oci-ansible-collection will be installed
                Default path for this is determined by ansible-galaxy installer.""",
    )

    parser.add_argument(
        "--version",
        help="""Users can use this flag to specify the version of oci-ansible-collection will be installed.
                To use the latest version don't set any value(recommended). If not specified the latest
                version will be used.
                Ex: 2.20.0

                Speciying --version along with --upgrade will result in a conflict
                Error will raised and installation will not continue.
                """,
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="""Runs the script in dry run mode i.e no network calls during installation and installation of dependecies""",
    )

    parser.add_argument(
        "--upgrade",
        action="store_true",
        help="""Users can specify this to upgrade the oci-ansible-collection and its required dependencies.
                This is will upgrade oci package and oci-ansible-collection to the latest one.
                Note: This will not upgrade ansible dependency to the latest version.

                Speciying --version along with --upgrade will result in a conflict
                Error will raised and installation will not continue.
                """,
    )

    args = parser.parse_args()

    installer = OciAnsibleCollectionInstaller(
        dry_run=args.dry_run,
        verbose=args.verbose,
        virtual_env_directory=args.virtual_env_dir,
        virtual_env_name=args.virtual_env_name,
        ansible_version=args.ansible_version,
        oci_ansible_collection_path=args.oci_ansible_collection_path,
        oci_ansible_collection_version=args.version,
        upgrade=args.upgrade,
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
