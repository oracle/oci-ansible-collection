# POST DEPLOYMENT STEPS FOR AWX V19.3 (deployed using solution hub)

## 1)Once the AWX deployment is complete. Go to RMS Jobs

![AWX_RMS_Job_1.jpeg](images/awx/AWX_RMS_Job_1.jpeg)

## 2)Click on Outputs

![AWX_RMS_outputs_2.png](images/awx/AWX_RMS_outputs_2.png)

## 3)Copy "awx_ui_ip" value and paste in the browser

![AWX_RMS_awx_ip_3.png](images/awx/AWX_RMS_awx_ip_3.png)

## 4)AWX Login page

![AWX_RMS_awx_login_page_4.png](images/awx/AWX_RMS_awx_login_page_4.png)

## 5)Type "admin"

![awx_login_page_5.png](images/awx/awx_login_page_5.png)

## 6)Go back to RMS Job output and copy "awx_login_password" value

![awx_password_copy_6.png](images/awx/awx_password_copy_6.png)

## 7)Go to AWX

![awx_login_pwd_paste_7.png](images/awx/awx_login_pwd_paste_7.png)

## 8)Paste the password and click on Log In

![awx_login_button_8.png](images/awx/awx_login_button_8.png)

## 9)Create a docker image for execution environment and publish the docker image in your tenancy docker registery

This docker image should install OCI Python SDK which is pre-requisite for OCI Ansible Collection.

- Refer:
  - <https://docs.ansible.com/automation-controller/latest/html/userguide/execution_environments.html#build-ee>
  - <https://www.oracle.com/webfolder/technetwork/tutorials/obe/oci/registry/index.html>

## 10)Go to Execution environments, click on OCI_EXECUTION_ENVIRONMENT, click edit, provide the newly created docker image name and save it

![edit_execution_env_8.1.png](images/awx/edit_execution_env_8.1.png)

## 11)Click on Credentials

![awx_add_creds_9.png](images/awx/awx_add_creds_9.png)

## 12)Click on Add

![awx_cred_add_button_10.png](images/awx/awx_cred_add_button_10.png)

## 13)Provide any name for credentials

![awx_cred_name_11.png](images/awx/awx_cred_name_11.png)

## 14)Search Organization

![awx_cred_org_12.png](images/awx/awx_cred_org_12.png)

## 15)Select OCI_ORG

![awx_org_select_13.png](images/awx/awx_org_select_13.png)

## 16)Click on Select Credential Type

![awx_cred_cred_type_14.png](images/awx/awx_cred_cred_type_14.png)

## 17)Select OCI

![awx_cred_type_oci_15.png](images/awx/awx_cred_type_oci_15.png)

## 18)You should see the newly created credential

![awx_cred_16.png](images/awx/awx_cred_16.png)

## 19)Now Click on Inventories

![click_inventories_17.png](images/awx/click_inventories_17.png)

## 20)Click on OCI_INVENTORY and then Click on Sources

![inventory_sources_18.png](images/awx/inventory_sources_18.png)

## 21)Click on Edit Source and Search for Credential

![inventory_creds_19.png](images/awx/inventory_creds_19.png)

## 22)Select the credential created in the previous step

![select_your_cred_20.png](images/awx/select_your_cred_20.png)

## 23)Click on Save

![save_inv_changes_21.png](images/awx/save_inv_changes_21.png)

## 24)Next step is to add project. so click on Projects

![add_project_22.png](images/awx/add_project_22.png)

## 25)Click on Add and provide the project name

![project_details_23.png](images/awx/project_details_23.png)

## 26)Search for Organization

![project_org_24.png](images/awx/project_org_24.png)

## 27)Select OCI_ORG

![project_oci_Org_25.png](images/awx/project_oci_Org_25.png)

## 28)Search for Execution environment

![project_ee_26.png](images/awx/project_ee_26.png)

## 29)Select OCI_EXECUTION_ENVIRONMENT

![project_ee_oci_27.png](images/awx/project_ee_oci_27.png)

## 30)Select Git

![project_type_28.png](images/awx/project_type_28.png)

## 31)Provide the Git repo url of your project

![project_repo_url_29.png](images/awx/project_repo_url_29.png)

## 32)Select "Clean" , "Delete" and "Update Revision on Launch"

![project_metadata_30.png](images/awx/project_metadata_30.png)

## 33)Click on Save

![save_project_31.png](images/awx/save_project_31.png)

## 34)Project creation status can be seen on the Jobs link

![project_jobs_32.png](images/awx/project_jobs_32.png)

## 35)Click on Inventories

![project_inv_33.png](images/awx/project_inv_33.png)

## 36)Select " OCI_INVENTORY" and click on Sources

![project_oci_inv_src_34.png](images/awx/project_oci_inv_src_34.png)

## 37)Click on Start sync process

![sync_src_35.png](images/awx/sync_src_35.png)

## 38)Click on Jobs to view status of inventory fetch

![inv_jobs_36.png](images/awx/inv_jobs_36.png)

## 39)Click on Templates

![add_template_37.png](images/awx/add_template_37.png)

## 40)Click on Add and select "Add job template"

![add_template_38.png](images/awx/add_template_38.png)

## 41)Provide Template details

![template_details_39.png](images/awx/template_details_39.png)

## 42)Search for the Inventory

![template_inv_40.png](images/awx/template_inv_40.png)

## 43)Select OCI_INVENTORY

![oci_inv_41.png](images/awx/oci_inv_41.png)

## 44)Search for the Project

![template_project_42.png](images/awx/template_project_42.png)

## 45)Select the project you created in the last step

![select_proj_43.png](images/awx/select_proj_43.png)

## 46)Search for Execution environment

![project_template_ee_44.png](images/awx/project_template_ee_44.png)

## 47)Select OCI_EXECUTION_ENVIRONMENT

![select_ee_45.png](images/awx/select_ee_45.png)

## 48)Click on Select a playbook

![playbook_46.png](images/awx/playbook_46.png)

## 49)Select a playbook to run

Note: these playbooks should be available in your project git repo
![actual_playbook_to_run_47.png](images/awx/actual_playbook_to_run_47.png)

## 50)Search for credentials

![template_cred_48.png](images/awx/template_cred_48.png)

## 51)Select OCI

![creds_49.png](images/awx/creds_49.png)

## 52)Select the creds you created

![my_creds_50.png](images/awx/my_creds_50.png)

## 53)Click on Save

![save_template_51.png](images/awx/save_template_51.png)

## 54)Click on Launch

![launch_template_52.png](images/awx/launch_template_52.png)

## 55)Click on Jobs to see template status

![template_in_jobs_status_53.png](images/awx/template_in_jobs_status_53.png)

## 56)Click on Hosts to see if the hosts are fetched or not

Note: If hosts are fetched that means dynamic inventory is available
![di_hosts_54.png](images/awx/di_hosts_54.png)
