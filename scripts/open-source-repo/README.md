This directory contains scripts and artifacts related to the open source
repo at OGHO.

# OGHO repo structure
## Content required to match the ansible role structure
- *library* : contains modules sources, utilities and doc fragments
- *meta*/main.yaml: role metadata

## Content to match what goes into Ansible repo
- *module_utils*
- *module_doc_fragments*
- *tests*/units
- *inventory-script* : contains oci_inventory.py and oci_inventory.ini

## Installer and uninstaller scripts
- `install.py`
- `uninstall.py`

## Documentation
- `README.md`
- `CONTRIBUTING.md`
- `CHANGELOG.md`
- `LICENSE.txt`

