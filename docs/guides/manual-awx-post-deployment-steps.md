# POST DEPLOYMENT STEPS FOR AWX V19.3 (deployed manually)

### 1)Once the AWX deployment is complete. Log In into AWX UI and add Execution environment. 
The OCI collection depends on the OCI Python SDK to run. 
To install the SDK, we have created a docker image which installs the OCI Python SDK.
![](images/awx/manual/ee_add_2.png)

### 2)Add details for the execution environment details. 
Provide the images value `iad.ocir.io/bmcs-dex-us-ashburn-1/awx:awxv19.2.2-latest`
![](images/awx/manual/ee_details_3.png)

### 3)Add organization.
![](images/awx/manual/org_add_1.png)

### 4)Add details for the Organization.
![](images/awx/manual/org_details_4.png)

### 5)Add credential type.
![](images/awx/manual/create_cred_type_5.png)

### 6)Provide credential type values.
Input Configuration:
```angular2html
fields:
  - id: user_ocid
    type: string
    label: User OCID
  - id: fingerprint
    type: string
    label: Fingerprint
  - id: tenant_ocid
    type: string
    label: Tenant OCID
  - id: region
    type: string
    label: Region
  - id: private_user_key
    type: string
    label: Private User Key
    secret: true
    multiline: true
required:
  - user_ocid
  - tenant_ocid
  - region
  - fingerprint
  - private_user_key
```
Injector Configuration:
```angular2html
env:
  OCI_CONFIG_FILE: '{{ tower.filename.config }}'
  OCI_USER_KEY_FILE: '{{ tower.filename.keyfile }}'
file:
  template.config: |-
    [DEFAULT]
    user={{ user_ocid }}
    fingerprint={{ fingerprint }}
    tenancy={{ tenant_ocid }}
    region={{ region }}
  template.keyfile: '{{ private_user_key }}'
```
![](images/awx/manual/cred_type_details_6.png)


### 7)Create Git repo and add the playbooks. Follow below folder structure:
```
├── collections
│   └── requirements.yml
└── inventory.oci.yml
```
The inventory.oci.yml file contains the following details for the inventory plugin:
```angular2html
$ cat inventory.oci.yml
plugin: oracle.oci.oci
regions: all
fetch_db_hosts: true
```
Create a [requirements file](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html#install-multiple-collections-with-a-requirements-file) at collections or requirements.yml that looks like the following string:
```angular2html
$ cat collections/requirements.yml
collections:
  - name: oracle.oci
```

### 8)Add Project and provide the details.
![](images/awx/project_metadata_30.png)

### 9)Add Inventory.
![](images/awx/manual/add_inventory_7.png)

### 10)Provide Inventory details.
![](images/awx/manual/inv_details_8.png)

### 11)Add Inventory source.
![](images/awx/manual/add_inv_src_9.png)

### 12)Add Inventory source details by providing proper values which you created in previous steps.
![](images/awx/manual/inv_src_details_10.png)

### 13)Finally synchronize the inventory to fetch the hosts/groups.
![](images/awx/sync_src_35.png)
Follow further steps from `AWX post deployment steps (deployed using Solution Hub)` starting from #36 till end. 
