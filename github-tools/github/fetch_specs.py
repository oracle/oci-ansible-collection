"""Copy spec files from git repositories into a central directory.
Format of spec file is a json serialized array of objects, each object containing location of the file to pull:
[
  {
    "name"       : "core",
    "repository" : "ssh://git@bitbucket.oci.oraclecorp.com:7999/commons/coreservices-api-spec.git",
    "file"       : "src/main/resources/coreservices-api-spec.yaml",
    "tag"        : "coreservices-api-spec-0.0.19"
  }
]
"""

import json
import os
import shutil
import sys

from pathlib import Path
from subprocess import call

SPECS_FILENAME = "specs.json"
TMP_DIR = "/tmp/spec_workspace"

def ensure_dir(path):
    try:
        path.mkdir(parents=True)
    except OSError:
        pass


def get_config(src):
    path = src + "/" + SPECS_FILENAME
    try:
        with open(path, 'r') as f:
            return json.loads(f.read())
    except Exception as ex:
        sys.stdout.write("Unable to load tools config file: %s\n" % ex)
        sys.exit(1)


def fetch(src, dest):
    config = get_config(src)

    ensure_dir(Path(dest))

    if os.path.isdir(TMP_DIR):
        shutil.rmtree(TMP_DIR)
    ensure_dir(Path(TMP_DIR))

    for spec in config:
        call(['git', 'clone', '-b', spec['tag'], spec['repository'], TMP_DIR + '/' + spec['name']])
        shutil.copyfile(TMP_DIR + '/' + spec['name'] + '/' + spec['file'], dest + '/' + spec['name'] + '.yaml')
