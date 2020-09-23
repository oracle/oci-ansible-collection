---
name: Bug report
about: Create a report to help us improve
title: ''
labels: ''
assignees: ''

---

## Issue Report

**Describe the issue**

A clear and concise description of what the issue is.

**Expected behavior**

A clear and concise description of what you expected to happen.

**Environment**

* OS version:

* Ansible version:

    insert output of `ansible --version` here

* OCI Python SDK version:

    insert output of `python -c "import oci;print(oci.__version__)"` here

* OCI Ansible Modules version:

    insert output of either one of these (based on the installation path):
`cat ~/.ansible/collections/ansible_collections/oracle/oci/MANIFEST.json | grep version`
`cat /usr/share/ansible/collections/ansible_collections/oracle/oci/MANIFEST.json | grep version`

**Ansible playbook to reproduce the issue**

    insert a sample playbook to reproduce the issue here(if relevant to the issue)
