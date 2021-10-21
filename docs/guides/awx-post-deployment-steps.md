# POST DEPLOYMENT STEPS FOR AWX V19.3 (deployed using solution hub)


### 1)Once the AWX deployment is complete. Go to RMS Jobs 

![](images/awx/AWX_RMS_Job_1.jpeg)


### 2)Click on Outputs
![](images/awx/AWX_RMS_outputs_2.png)


### 3)Copy "awx_ui_ip" value and paste in the browser.
![](images/awx/AWX_RMS_awx_ip_3.png)


### 4)AWX Login page
![](images/awx/AWX_RMS_awx_login_page_4.png)


### 5)Type "admin"
![](images/awx/awx_login_page_5.png)


### 6)Go back to RMS Job output and copy "awx_login_password" value
![](images/awx/awx_password_copy_6.png)


### 7)Go to AWX
![](images/awx/awx_login_pwd_paste_7.png)


### 8)Paste the password and click on Log In
![](images/awx/awx_login_button_8.png)


### 9)Click on Credentials
![](images/awx/awx_add_creds_9.png)


### 10)Click on Add
![](images/awx/awx_cred_add_button_10.png)


### 11)Provide any name for credentials
![](images/awx/awx_cred_name_11.png)


### 12)Search Organization
![](images/awx/awx_cred_org_12.png)


### 13)Select OCI_ORG
![](images/awx/awx_org_select_13.png)


### 14)Click on Select Credential Type
![](images/awx/awx_cred_cred_type_14.png)


### 15)Select OCI
![](images/awx/awx_cred_type_oci_15.png)


### 16)You should see the newly created credential
![](images/awx/awx_cred_16.png)


### 17)Now Click on Inventories
![](images/awx/click_inventories_17.png)


### 18)Click on OCI_INVENTORY and then Click on Sources
![](images/awx/inventory_sources_18.png)


### 19)Click on Edit Source and Search for Credential
![](images/awx/inventory_creds_19.png)


### 20)Select the credential created in the previous step
![](images/awx/select_your_cred_20.png)


### 21)Click on Save
![](images/awx/save_inv_changes_21.png)


### 22)Next step is to add project. so click on Projects
![](images/awx/add_project_22.png)


### 23)Click on Add and provide the project name
![](images/awx/project_details_23.png)


### 24)Search for Organization
![](images/awx/project_org_24.png)


### 25)Select OCI_ORG
![](images/awx/project_oci_Org_25.png)


### 26)Search for Execution environment
![](images/awx/project_ee_26.png)


### 27)Select OCI_EXECUTION_ENVIRONMENT
![](images/awx/project_ee_oci_27.png)


### 28)Select Git
![](images/awx/project_type_28.png)


### 29)Provide the Git repo url of your project
![](images/awx/project_repo_url_29.png)


### 30)Select "Clean" , "Delete" and "Update Revision on Launch "
![](images/awx/project_metadata_30.png)


### 31)Click on Save
![](images/awx/save_project_31.png)


### 32)Project creation status can be seen on the Jobs link
![](images/awx/project_jobs_32.png)


### 33)Click on Inventories
![](images/awx/project_inv_33.png)


### 34)Select " OCI_INVENTORY" and click on Sources
![](images/awx/project_oci_inv_src_34.png)


### 35)Click on Start sync process
![](images/awx/sync_src_35.png)


### 36)Click on Jobs to view status of inventory fetch
![](images/awx/inv_jobs_36.png)


### 37)Click on Templates
![](images/awx/add_template_37.png)


### 38)Click on Add and select "Add job template"
![](images/awx/add_template_38.png)



### 39)Provide Template details
![](images/awx/template_details_39.png)



### 40)Search for the Inventory
![](images/awx/template_inv_40.png)


### 41)Select OCI_INVENTORY
![](images/awx/oci_inv_41.png)



### 42)Search for the Project
![](images/awx/template_project_42.png)


### 43)Select the project you created in the last step
![](images/awx/select_proj_43.png)



### 44)Search for Execution environment
![](images/awx/project_template_ee_44.png)


### 45)Select OCI_EXECUTION_ENVIRONMENT
![](images/awx/select_ee_45.png)


### 46)Click on Select a playbook
![](images/awx/playbook_46.png)



### 47)Select a playbook to run
Note: these playbooks should be available in your project git repo
![](images/awx/actual_playbook_to_run_47.png)



### 48)Search for credentials
![](images/awx/template_cred_48.png)



### 49)Select OCI
![](images/awx/creds_49.png)



### 50)Select the creds you created
![](images/awx/my_creds_50.png)



### 51)Click on Save
![](images/awx/save_template_51.png)



### 52)Click on Launch
![](images/awx/launch_template_52.png)


### 53)Click on Jobs to see template status
![](images/awx/template_in_jobs_status_53.png)



### 54)Click on Hosts to see if the hosts are fetched or not
Note: If hosts are fetched that means dynamic inventory is available
![](images/awx/di_hosts_54.png)



### Similarly, you can create dynamic inventory job template and launch it.
###You can also refer to [this video](https://objectstorage.us-ashburn-1.oraclecloud.com/n/bmcs-dex-us-ashburn-1/b/ansible_onboarding_resources/o/awx%20v19.3%20post%20deployment%20stepsawx-post-installation-steps.mov) for post deployment steps for awx v19.3