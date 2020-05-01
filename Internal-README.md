# Oracle Cloud Infrastructure Ansible Modules

## Updating with latest specs and enabled features from OCI Python SDK

Clone the Python SDK locally and run the following script to copy the up-to-date poms and codegenConfig:

python scripts/copy_python_sdk_poms.py --python-sdk-dir ~/dev/SDK/python-sdk --ansible-collections-repo-dir ~/dev/SDK/ansible_collections_oci

Note: this script is Python 2 compatible *only*

If there are features or services that are enabled in the Python SDK that you do not want to copy into Ansible you can add them to the relevant blacklist in this repo at python-sdk-copy-features-config.yaml.

# Generating modules

To generate all services, run the following command from the root directory of the repo:
`make gen`

To generate a single service run the following command from the root directory of the repo (replace identity with the service you want to target):
`mvn install -pl poms/identity/pom.xml`
