# OCI Ansible AWX

## Introduction

[Red Hat Ansible Tower](https://docs.ansible.com/ansible-tower/latest/html/administration/index.html) and [AWX](https://github.com/ansible/awx) can centralize and control your IT infrastructure with a visual dashboard, role-based access control, job scheduling, integrated notifications, and graphical inventory management. Its task engine is built on Ansible. AWX is the open source community project and the upstream project for Tower.
Oracle Cloud Infrastructure (OCI) supports installing AWX v19.3 quickly on Oracle Compute instance using the Resource Manager service.

## Use of Ansible modules in AWX templates

- Usage of Ansible modules in AWX templates is similar to writing any ansible playbook.
- Please refer to [this example awx template file](https://github.com/oracle/oci-ansible-collection/blob/master/docs/guides/awx/awx_samples/list_objects.yaml)
- For this sample template we need to pass 2 runtime variables i.e. compartment id and namespace name
![AWX_runtime_variable.png](images/awx/AWX_runtime_variable.png)

## Use of OCI Inventory plugin in AWX

- OCI Dynamic Inventory is already setup in AWX as part of the installation. To confirm please check the groups and hosts values under Inventories.
- Please refer to [this example](https://github.com/oracle/oci-ansible-collection/blob/master/docs/guides/awx/awx_samples/sample_dynamic_inventory.yaml) of awx template file which uses dynamic inventory
- In this example we are specifying the `Hosts` value as `AnsibleIntegrationTestCompartment1` so this playbook will run only for the hosts which are part of this group.

## Troubleshooting

- To find the logs or status of a task, click on `Jobs` and you should see the running tasks.
- Make sure your provided user credentials are correct
- Currently, we are using [execution environment](https://docs.ansible.com/ansible-tower/latest/html/administration/external_execution_envs.html) to install the python sdk, which is pre-requisite for running the OCI Ansible Collection. If your awx job fails with `OCI Python SDK required` error then this can be one of the issue.
- It is recommended to keep the verbosity level to `Debug` so that it is easier to trace any issues.
- Make sure you have 1 free public ip limit, which will be required for AWX deployment
