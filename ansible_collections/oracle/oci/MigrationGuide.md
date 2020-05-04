## Ansible Collections Migration Guide


#### Identity

|   old name                             |    new name                              |  migration notes
|----------------------------------------|------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
|oci_ad_facts                            |  oci_identity_availability_domain_facts  |  breaking changes:
|                                        |                                          |  <ul><li>compartment_id parameter no longer has alias 'id'</li></ul>
|                                        |
|oci_api_key                             |  oci_identity_api_key                    |  breaking changes:
|                                        |                                          | <ul><li>`api_signing_key` param is replaced by `key` param</li> <li> `api_key_id` param has been removed<ul><li>users should use new `fingerprint` instead to uniquely identify an api key when attempting to perform a delete</li></ul></li></ul>
|                                        |
|oci_api_key_facts                       |  oci_identity_api_key_facts              |  breaking changes:
|                                        |                                          |  <ul><li>`api_key_id` parameter is removed <ul><li> users should manually filter in their playbook if they want to isolate a single api_key </li></ui></li></ul>
|                                        |
|oci_auth_token                          |  oci_identity_auth_token                 |  no breaking changes
|                                        | 
|oci_auth_token_facts                    |  oci_identity_auth_token_facts           |  no breaking changes
|                                        |
|oci_compartment                         |  oci_identity_compartment                |  breaking changes:
|                                        |                                          |  <ul><li>'compartment_id' parameter can no longer be used when creating a compartment to specify the parent compartment id<ul><li>users must use 'parent_compartment_id' for this purpose</li></ul></li> <li>If you specify 'compartment_id' == 'tenancy_id' the request will be treated just like any other update compartment request and will attempt to update the root compartment (this was previously not the case, the module would interpret this as a create under the root compartment). Note that you can update the description of the root compartment, but not the name.</li>  <li> 'work_request' field on response is no longer returned, the module still waits internally on the work request it just does not return it</li> </ul> 
|                                        |                                          |  notes:
|                                        |                                          |  <ul><li>these tests need a way of running weekly</li></ul>
|                                        |                                          |  
|oci_compartment_facts                   |  oci_identity_compartment_facts          |  breaking changes:
|                                        |                                          |  <ul><li>fetch_subcompartments and depth parameters no longer exist<ul><li>if you want to fetch information about a single level of subcompartments, you must specify the input parameter 'parent_compartment_id'</li><li>if you want to fetch information about a specific compartment, you must specify the input parameter 'compartment_id'</li><li>there is a a new parameter 'compartment_id_in_subtree' for listing full component hierarchies <ul><li> when this parameter is set to true, the entire compartment hierarchy under 'parent_compartment_id' will be returned (note this does not return the parent compartment itself)</li></ul></li></ul></li></ul>
|                                        |
|oci_cost_tracking_tag_facts             |  oci_identity_cost_tracking_tag_facts    |  breaking changes:
|                                        |                                          |  <ul><li>response field is now 'cost_tracking_tags' instead of 'tags'</li></ul>
|                                        |
|oci_customer_secret_key                 |  oci_identity_customer_secret_key        |  no breaking changes
|                                        |
|oci_customer_secret_key                 |  oci_identity_customer_secret_key_facts  |  breaking changes:
|                                        |                                          |  <ul><li>there is no longer a `customer_secret_key_id` parameter to filter to a specific key id</li></ul> 
|                                        |
|oci_dynamic_group                       |  oci_identity_dynamic_group              |  no breaking changes
|                                        |
|oci_dynamic_group_facts                 |  oci_identity_dynamic_group_facts        |  no breaking changes
|                                        |
|oci_fault_domain_facts                  |  oci_identity_fault_domain_facts         |  no breaking changes
|                                        |
|oci_group                               |  oci_identity_group                      |  breaking changes:
|                                        |                                          |  <ul><li>The following parameters no longer exist: users, purge_user_memberships, delete_user_memberships, force <ul><li>You must use oci_identity_user_group_membership to manage group memberships</li></ul></li> <li>There is now a 'compartment_id' parameter which is required for several operations. Previously this defaulted to the tenancy ID, but now you must supply it explicitly</li></ul>
|                                        |                                          |  
|oci_group_facts                         |  oci_identity_group_facts                |  breaking changes:
|                                        |                                          |  <ul><li>No longer returns the 'members' property containing the users in a group<ul><li> Users in a group can be determined using the oci_identity_user_group_membership_facts module</li></ul></li></ul>
|                                        |
|oci_identity_identity_provider_actions  |  oci_identity_provider_actions           |  no breaking changes
|                                        |
|oci_identity_provider                   |  oci_identity_provider                   |  breaking changes:
|                                        |                                          |  <ul><li>'protocol' parameter no longer has a default value, so it must be explicitly provided</li></ul>
|                                        |
|oci_identity_provider_facts             |  oci_identity_provider_facts             |  breaking changes:
|                                        |                                          |  <ul><li>'protocol' parameter no longer has a default value, so it must be explicitly provided when listing Identity Providers</li></ul>
|                                        |
|oci_identity_tag_default                |  oci_identity_tag_default                |  no breaking changes (was newly generated in the old modules)
|                                        |
|oci_identity_tag_default_facts          |  oci_identity_tag_default_facts          |  no breaking changes (was newly generated in the old modules)
|                                        |
|oci_idp_group_mapping                   |  oci_identity_idp_group_mapping          |  no breaking changes
|                                        |
|oci_idp_group_mapping_facts             |  oci_identity_idp_group_mapping_facts    |  no breaking changes
|                                        |
|oci_policy                              |  oci_identity_policy                     |  breaking changes:
|                                        |                                          |  <ul><li>policy_document field no longer exists.<ul><li>An easy replacement for this field is to use built-in ansible functionality to read a 'policy_document' file into the `statements` parameter:`statements: "{{ lookup('file', policyfile.path).splitlines() }}"`</li></ul></li></ul>
|                                        |
|oci_policy_facts                        |  oci_identity_policy_facts               |  no breaking changes
|                                        |
|oci_region_facts                        |  oci_identity_region_facts               |  no breaking changes
|                                        |
|oci_region_subscription_facts           |  oci_identity_region_subscription_facts  |  breaking changes:
|                                        |                                          |  <ul><li>tenancy_id parameter no longer has alias 'id'</li></ul>
|                                        |
|oci_smtp_credential                     |  oci_identity_smtp_credential            |  no breaking changes
|                                        |
|oci_smtp_credential_facts               |  oci_identity_smtp_credential_facts      |  no breaking changes
|                                        |
|oci_tag                                 |  oci_identity_tag                        |  breaking changes:
|                                        |                                          |  <ul><li>existing 'tag_name' parameter is now 'name'</li><li>state: absent now deletes a tag instead of retiring it<ul><li>to retire a tag you must use is_retired: 'yes'</li> <li>a tag must be retired before it is deleted</li></ul></li> <li>'reactivate' parameter is no longer supported<ul><li>instead, to reactivate a tag you must use is_retired: 'no'</li></ul></li></ul>
|                                        |                                          |  
|oci_tag_facts                           |  oci_identity_tag_facts                  |  breaking changes:
|                                        |                                          |  <ul><li>'tag_name' no longer has 'name' alias</li></ul>
|                                        |
|oci_tag_namespace                       |  oci_identity_tag_namespace              |  breaking changes:
|                                        |                                          |  <ul><li>state: 'absent' now deletes a tag namespace instead of retiring it<ul><li>instead, to retire a namespace you must use is_retired: 'yes'</li></ul></li><li>'reactivate' parameter is no longer supported<ul><li>instead, to reactivate a namespace you must use is_retired: 'no'</li></ul></li></ul>
|                                        | 
|oci_tag_namespace_facts                 |  oci_identity_tag_namespace_facts        |  no breaking changes
|                                        |
|oci_tenancy_facts                       |  oci_identity_tenancy_facts              |  no breaking changes
|                                        |
|oci_user                                |  oci_identity_user                       |  breaking changes:
|                                        |                                          |  <ul><li>The following parameters no longer exist: create_or_reset_ui_password, purge_group_memberships, delete_group_memberships, blocked, user_groups<ul><li> You must use oci_identity_user_group_membership to manage group memberships</li> <li>You must use oci_identity_ui_password to perform the create_or_reset_ui_password operation</li></ul></li> <li>There is now a 'compartment_id' parameter which is required for several operations. Previously this defaulted to the tenancy ID, but now you must supply it explicitly</li><li>functionality of the "create_or_reset_ui_password" parameter is moved to new module `oci_identity_ui_password`</li></ul>
|                                        |                                          | 

#### Network

|  old name                                                       |  new name                                                                         |  migration notes                                                                                                                                                     |
|-----------------------------------------------------------------|-----------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|oci_cpe                                                          |  oci_network_cpe                                                                  |  no breaking changes       
|                                                                 |                                                                                   |
|oci_cpe_facts                                                    |  oci_network_cpe_facts                                                            |  no breaking changes  
|                                                                 |                                                                                                                                                      
|oci_cross_connect                                                |  oci_network_cross_connect                                                        |  no breaking changes      
|                                                                 |                                                                                        
|oci_cross_connect_facts                                          |  oci_network_cross_connect_facts                                                  |  no breaking changes                                                                                                                                                 |
|                                                                 |                                                                                   |  The generated module fixes the bug in the old module where list is called for getting a specific resource. The generated module fixes the bug.                      |
|                                                                 |
|oci_cross_connect_group                                          |  oci_network_cross_connect_group                                                  |  no breaking changes                                                                                                                                                 |
|                                                                 |
|oci_cross_connect_group_facts                                    |  oci_network_cross_connect_group_facts                                            |  no breaking changes                                                                                                                                                 |
|                                                                 |                                                                                   |  The generated module fixes the bug in the old module where list is called for getting a specific resource. The generated module fixes the bug.                      |
|                                                                 |
|oci_cross_connect_location_facts                                 |  oci_network_cross_connect_location_facts                                         |  no breaking changes                                                                                                                                                 |
|                                                                 |
|oci_cross_connect_port_speed_shape_facts                         |  oci_network_cross_connect_port_speed_shape_facts                                 |  no breaking changes                                                                                                                                                 |
|                                                                 |
|oci_cross_connect_status_facts                                   |  oci_network_cross_connect_status_facts                                           |  breaking changes:                                                                                                                                                   |
|                                                                 |                                                                                   |  <ul><li>Return field in new module is cross_connect_status instead of cross_connect_statuses</li></ul>                                                              |
|                                                                 |
|oci_dhcp_options                                                 |  oci_network_dhcp_options                                                         |  breaking changes:                                                                                                                                                   |
|                                                                 |                                                                                   |  <ul><li>The following parameters no longer exist: purge_dhcp_options, delete_dhcp_options</li></ul>                                                                 |
|                                                                 |
|oci_dhcp_options_facts                                           |  oci_network_dhcp_options_facts                                                   |  breaking changes:                                                                                                                                                   |
|                                                                 |                                                                                   |  <ul><li>Return field in new module is dhcp_options instead of dhcp_options_list</li></ul>                                                                           |
|                                                                 |
|oci_drg                                                          |  oci_network_drg                                                                  |  no breaking changes                                                                                                                                                 |
|                                                                 |
|oci_drg_attachment                                               |  oci_network_drg_attachment                                                       |  no breaking changes                                                                                                                                                 |
|                                                                 |
|oci_drg_attachment_facts                                         |  oci_network_drg_attachment_facts                                                 |  no breaking changes                                                                                                                                                 |
|                                                                 |
|oci_drg_facts                                                    |  oci_network_drg_facts                                                            |  no breaking changes                                                                                                                                                 |
|                                                                 |
|oci_fast_connect_provider_service_facts                          |  oci_network_fast_connect_provider_service_facts                                  |  no breaking changes                                                                                                                                                 |
|                                                                 |
|oci_fast_connect_provider_virtual_circuit_bandwidth_shape_facts  |  oci_network_fast_connect_provider_service_virtual_circuit_bandwidth_shape_facts  |  breaking changes:                                                                                                                                                   |
|                                                                 |                                                                                   |  <ul><li>Return field in new module is fast_connect_provider_service_virtual_circuit_bandwidth_shapes instead of fast_connect_provider_virtual_circuit_bandwidth_shapes</li><li> provider_service_id parameter no longer has alias 'id' </li></ul> 
|                                                                 |                                                                                   |                                                                                                             
|oci_internet_gateway                                             |  oci_network_internet_gateway                                                     |  breaking changes:                                                                                                                                                   |
|                                                                 |                                                                                   |  <ul><li>is_enabled parameter in the new module does not have the alias enabled</li></ul>                                                                            |
|                                                                 |
|oci_internet_gateway_facts                                       |  oci_network_internet_gateway_facts                                               |  no breaking changes                                                                                                                                                 |
|                                                                 |
|oci_ip_sec_connection                                            |  oci_network_ip_sec_connection                                                    |  breaking changes:                                                                                                                                                   |
|                                                                 |                                                                                   |  <ul><li>ipsc_id parameter no longer has alias 'id'</li></ul>                                                                                                        |
|                                                                 |
|oci_ip_sec_connection_device_config_facts                        |  oci_network_ip_sec_connection_device_config_facts                                |  no breaking changes                                                                                                                                                 |
|                                                                 |
|oci_ip_sec_connection_device_status_facts                        |  oci_network_ip_sec_connection_device_status_facts                                |  no breaking changes                                                                                                                                                 |
|                                                                 |
|oci_ip_sec_connection_facts                                      |  oci_network_ip_sec_connection_facts                                              |  no breaking changes                                                                                                                                                 |
|                                                                 |
|oci_letter_of_authority_facts                                    |  oci_network_letter_of_authority_facts                                            |  breaking changes:                                                                                                                                                   |
|                                                                 |                                                                                   |  <ul><li>Return field in new module is letter_of_authority instead of letter_of_authorities. Also the return field in the new module is a dictionary instead of a list. </li></ul>     |
|                                                                 |
|oci_local_peering_gateway                                        |  oci_network_local_peering_gateway                                                |  breaking changes:                                                                                                                                                   |
|                                                                 |                                                                                   |  <ul><li>The following parameters no longer exist: skip_exhaustive_search_for_lpg_peerings, peer_id. Need to use oci_network_local_peering_gateway_actions to connect LPGs.  </li></ul>|
|                                                                 |                           
|oci_local_peering_gateway_facts                                  |  oci_network_local_peering_gateway_facts                                          |  no breaking changes                                                                                                                                                 |
|                                                                 |
|oci_nat_gateway                                                  |  oci_network_nat_gateway                                                          |  no breaking changes                                                                                                                                                 |
|                                                                 |
|oci_nat_gateway_facts                                            |  oci_network_nat_gateway_facts                                                    |  no breaking changes                                                                                                                                                 |
|                                                                 |
|oci_network_security_group                                       |  oci_network_security_group                                                       |  no breaking changes                                                                                                                                                 |
|                                                                 |
|oci_network_security_group_facts                                 |  oci_network_security_group_facts                                                 |  no breaking changes                                                                                                                                                 |
|                                                                 |
|oci_peer_region_for_remote_peering_facts                         |  oci_network_peer_region_for_remote_peering_facts                                 |  breaking changes:                                                                                                                                                   |
|                                                                 |                                                                                   |  <ul><li>Return field in new module is peer_region_for_remote_peerings instead of peer_region_for_remote_peering </li></ul>                                          |
|                                                                 |
|oci_private_ip                                                   |  oci_network_private_ip                                                           |  no breaking changes                                                                                                                                                 |
|                                                                 |
|oci_private_ip_facts                                             |  oci_network_private_ip_facts                                                     |  no breaking changes                                                                                                                                                 |
|                                                                 |
|oci_public_ip                                                    |  oci_network_public_ip                                                            |  breaking changes:                                                                                                                                                   |
|                                                                 |                                                                                   |  <ul><li>New module adds a new module parameter scope and it is required for creating the public ip </li></ul>                                                       |
|                                                                 |
|oci_public_ip_facts                                              |  oci_network_public_ip_facts                                                      |  no breaking changes                                                                                                                                                 |
|                                                                 |
|oci_remote_peering_connection                                    |  oci_network_remote_peering_connection                                            |  breaking changes:                                                                                                                                                   |
|                                                                 |                                                                                   |  <ul><li>The following parameters no longer exist: peer_id, peer_region_name. Need to use oci_network_remote_peering_connection_actions module for connecting RPCs. </li></ul>         |
|                                                                 |
|oci_remote_peering_connection_facts                              |  oci_network_remote_peering_connection_facts                                      |  no breaking changes                                                                                                                                                 |
|                                                                 | 
|oci_route_table                                                  |  oci_network_route_table                                                          |  breaking changes:                                                                                                                                                   |
|                                                                 |                                                                                   |  <ul><li>The following parameters no longer exist: purge_route_rules, delete_route_rules</li></ul>                                                                   |
|                                                                 |
|oci_route_table_facts                                            |  oci_network_route_table_facts                                                    |  no breaking changes                                                                                                                                                 |
|                                                                 |
|oci_security_list                                                |  oci_network_security_list                                                        |  breaking changes:                                                                                                                                                   |
|                                                                 |                                                                                   |  <ul><li>The following parameters no longer exist: purge_security_rules, delete_security_rules</li></ul>                                                             |
|                                                                 |
|oci_security_list_facts                                          |  oci_network_security_list_facts                                                  |  no breaking changes                                                                                                                                                 |
|                                                                 |
|oci_security_rule_actions                                        |  oci_network_security_rule_actions                                                |  no breaking changes                                                                                                                                                 |
|                                                                 |
|oci_security_rule_facts                                          |  oci_network_security_rule_facts                                                  |  no breaking changes                                                                                                                                                 |
|                                                                 |
|oci_service_facts                                                |  oci_network_service_facts                                                        |  no breaking changes                                                                                                                                                 |
|                                                                 |
|oci_service_gateway                                              |  oci_network_service_gateway                                                      |  no breaking changes                                                                                                                                                 |
|                                                                 |
|oci_service_gateway_facts                                        |  oci_network_service_gateway_facts                                                |  no breaking changes                                                                                                                                                 |
|                                                                 |
|oci_subnet                                                       |  oci_network_subnet                                                               |  no breaking changes                                                                                                                                                 |
|                                                                 |
|oci_subnet_facts                                                 |  oci_network_subnet_facts                                                         |  no breaking changes                                                                                                                                                 |
|                                                                 |
|oci_vcn                                                          |  oci_network_vcn                                                                  |  no breaking changes                                                                                                                                                 |
|                                                                 |
|oci_vcn_facts                                                    |  oci_network_vcn_facts                                                            |  no breaking changes                                                                                                                                                 |
|                                                                 |
|oci_virtual_circuit                                              |  oci_network_virtual_circuit                                                      |  breaking changes:                                                                                                                                                   |
|                                                                 |                                                                                   |  <ul><li>The following parameters no longer exist: purge_cross_connect_mappings, delete_cross_connect_mappings,delete_public_prefixes <ul><li>To add/delete public prefixes, use oci_network_virtual_circuit_actions module</li></ul></li></ul>                                                 |
|                                                                 |
|oci_virtual_circuit_bandwidth_shape_facts                        |  oci_network_virtual_circuit_bandwidth_shape_facts                                |  no breaking changes                                                                                                                                                 |
|                                                                 |
|oci_virtual_circuit_facts                                        |  oci_network_virtual_circuit_facts                                                |  no breaking changes                                                                                                                                                 |
|                                                                 |                                                       
|oci_virtual_circuit_public_prefix_facts                          |  oci_network_virtual_circuit_public_prefix_facts                                  |  breaking changes:                                                                                                                                                   |
|                                                                 |                                                                                   |  <ul><li>virtual_circuit_id parameter no longer has alias 'id' </li></ul>                                                                                                              |
|                                                                 |
|oci_vnic                                                         |  oci_network_vnic                                                                 |  no breaking changes                                                                                                                                                 |
|                                                                 |
|oci_vnic_facts                                                   |  oci_network_vnic_facts                                                           |  no breaking changes                                                                                                                                                 |


#### Compute

|old name                                        |  new name                                                          |  migration notes                                                                                                                                                                                              |
|------------------------------------------------|--------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|oci_app_catalog_listing_agreement               |  oci_compute_app_catalog_listing_resource_version_agreement_facts  |  breaking changes:                                                                                                                                                                                            |
|                                                |                                                                    |  <ul><li>New module is a facts module</li> <li>New module does not have state parameter</li><li>listing_id parameter in the new module does not have the alias id</li><li>resource_version parameter in the new module does not have the alias version</li><li>Return field in in new module is app_catalog_listing_resource_version_agreement instead of app_catalog_listing_agreement</li></ul>                                                                                                                                                                                                                                                                                                      |                                                                                       |
|                                                |
|oci_app_catalog_listing_facts                   |  oci_compute_app_catalog_listing_facts                             |  no breaking changes                                                                                                                                                                                          |
|                                                |
|oci_app_catalog_listing_resource_version_facts  |  oci_compute_app_catalog_listing_resource_version_facts            |  breaking changes:                                                                                                                                                                                            |
|                                                |                                                                    |  <ul><li>listing_id parameter in the new module does not have the alias id</li></ul>                                                                                                                                            |
|                                                |
|oci_app_catalog_subscription                    |  oci_compute_app_catalog_subscription                              |  no breaking changes                                                                                                                                                                                          |
|                                                |
|oci_app_catalog_subscription_facts              |  oci_compute_app_catalog_subscription_facts                        |  no breaking changes                                                                                                                                                                                          |
|                                                |
|oci_boot_volume_attachment                      |  oci_compute_boot_volume_attachment                                |  breaking changes:                                                                                                                                                                                            |
|                                                |                                                                    |  <ul><li>New module adds a new module parameter availability_domain and it is required for creating the boot volume attachment</li></ul>                                                                                        |
|                                                |
|oci_boot_volume_attachment_facts                |  oci_compute_boot_volume_attachment_facts                          |  no breaking changes                                                                                                                                                                                          |
|                                                |
|oci_console_history                             |  oci_compute_instance_console_history                              |  breaking changes:                                                                                                                                                                                            |
|                                                |                                                                    |  <ul><li>New module adds a new module parameter compartment_id and it is required for creating the console history</li></ul>                                                                                                    |
|                                                |
|oci_console_history_content_facts               |  oci_compute_instance_console_history_content_facts                |  breaking changes:                                                                                                                                                                                            |
|                                                |                                                                    |  <ul><li>New module does not have dest parameter. Returns data instead of writing it to a file (specified by dest parameter in the old module)</li><li>Return field name in the new module is instance_console_history_content instead of console_history_content</li></ul>                                                                        |
|                                                |
|oci_console_history_facts                       |  oci_compute_instance_console_history_facts                        |  no breaking changes                                                                                                                                                                                          |
|                                                |
|oci_image                                       |  oci_compute_image                                                 |  breaking changes:                                                                                                                                                                                            |
|                                                |                                                                    |  <ul><li>image_source_details.source_type parameter no longer has alias 'destination_type' </li> <li>image_source_details.bucket_name parameter no longer has alias 'bucket' </li> <li>image_source_details.namespace_name parameter no longer has alias 'namespace' </li>  <li>image_source_details.object_name parameter no longer has alias 'object'</li></ul>                                                                                                                            
|                                                |                                                                    |                                                                                                                                                                                    
|oci_image_actions                               |  oci_compute_image_actions                                         |  no breaking changes                                                                                                                                                                                          |
|                                                |
|oci_image_facts                                 |  oci_compute_image_facts                                           |  no breaking changes                                                                                                                                                                                          |
|                                                |
|oci_instance                                    |  oci_compute_instance                                              |  breaking changes:                                                                                                                                                                                            |
|                                                |                                                                    |  <ul><li>Experimental mode features not available anymore. New module does not have boot_volume_details and volume_details parameters. The new module does not return boot_volume_attachment and volume_attachments.</li><li>state parameter does not support the following values: running, stopped, reset and softreset. These operations moved to the actions module oci_compute_instance_actions. </li> <li>primary_public_ip and primary_private_ip are not returned by the new module</li></ul>  
|                                                |                                                                    |                                                                                                                                   |
|oci_instance_console_connection                 |  oci_compute_instance_console_connection                           |  breaking changes:                                                                                                                                                                                            |
|                                                |                                                                    |  <ul><li>New module adds a new module parameter compartment_id and it is required for creating the console connection</li> <li>In the new module, public_key parameter takes the actual key as input instead of the file containing it </li></ul>                                                                                                |
|                                                | 
|oci_instance_console_connection_facts           |  oci_compute_instance_console_connection_facts                     |  no breaking changes                                                                                                                                                                                          |
|                                                |
|oci_instance_credentials_facts                  |  oci_compute_instance_credentials_facts                            |  no breaking changes                                                                                                                                                                                          |
|                                                |
|oci_instance_facts                              |  oci_compute_instance_facts                                        |  breaking changes:                                                                                                                                                                                            |
|                                                |                                                                    |  <ul><li>Experimental mode features not available anymore i.e boot_volume_attachment and volume_attachments are not returned by the new module.</li><li>primary_public_ip and primary_private_ip are not returned by the new module</li></ul>                                                                       |
|                                                |                                                                    |                                                                                                                                    |
|oci_shape_facts                                 |  oci_compute_shape_facts                                           |  no breaking changes                                                                                                                                                                                          |
|                                                |
|oci_vnic_attachment                             |  oci_compute_vnic_attachment                                       |  breaking changes:                                                                                                                                                                                            |
|                                                |                                                                    |  <ul><li>create_vnic_details parameter no longer has alias 'vnic'</li></ul>                                                                                                                                                     |
|                                                |
|oci_vnic_attachment_facts                       |  oci_compute_vnic_attachment_facts                                 |  no breaking changes                                                                                                                                                                                          |
|                                                |
|oci_volume_attachment                           |  oci_compute_volume_attachment                                     |  breaking changes:                                                                                                                                                                                            |
|                                                |                                                                    |  <ul><li>New module adds a new module parameter compartment_id and it is required for creating the volume attachment</li></ul>                                                                                                  |
|                                                |
|oci_volume_attachment_facts                     |  oci_compute_volume_attachment_facts                               |  no breaking changes                                                                                                                                                                                          |                                                                                                                                                                                               |


#### Compute Management

|old name                           |  new name                                             |  migration notes
|-----------------------------------|-------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
|oci_instance_configuration         |  oci_compute_management_instance_configuration        |  no breaking changes
|                                   |
|oci_instance_configuration_facts   |  oci_compute_management_instance_configuration_facts  |  no breaking changes
|                                   |
|oci_instance_pool                  |  oci_compute_management_instance_pool                 |  breaking changes:
|                                   |                                                       |  <ul><li>New module does not support the following state parameter values: stopped, running, reset and softreset. Use the actions module oci_compute_management_instance_pool_actions instead.</li></ul>
|                                   |
|oci_instance_pool_actions          |  oci_compute_management_instance_pool_actions         |  no breaking changes
|                                   |
|oci_instance_pool_facts            |  oci_compute_management_instance_pool_facts           |  breaking changes:
|                                   |                                                       |  <ul><li>New module does not return the attributes placement_configurations and load_balancers when listing instance pools using compartment_id. To get this information call this module using instance_pool_id.</li></ul>
|                                   |
|oci_instance_pool_instances_facts  |  oci_compute_management_instance_pool_instance_facts  |  breaking changes:
|                                   |                                                       |  <ul><li>instance_pool_id parameter no longer has alias 'id'</li><li>Returns fields mentioned InstanceSummary instead of Instance. You can use oci_compute_instance_facts to get the complete instance information.</li></ul>
|                                   |                                                       |  


##### Blockstorage

|old name                                   |  new name                                                |  migration notes                                                                                                                                                                          |
|-------------------------------------------|----------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|oci_boot_volume                            |  oci_blockstorage_boot_volume                            |  breaking changes:                                                                                                                                                                        |
|                                           |                                                          |  <ul><li>Experimental mode features not available anymore i.e new module does not have the lookup_attached_instance module parameter and also does not return attached_instance_information</li> <li>New module does not have wait_for_copy and copy_timeout suboptions for source_details module parameter. Waiting till the copy is done, is the default behaviour in the new module.</li></ul>       
|                                           |
|oci_boot_volume_facts                      |  oci_blockstorage_boot_volume_facts                      |  breaking changes:                                                                                                                                                                        |
|                                           |                                                          |  <ul><li>Experimental mode features not available anymore i.e new module does not have the lookup_attached_instance module parameter and also does not return attached_instance_information</li></ul>       |
|                                           |
|oci_volume                                 |  oci_blockstorage_volume                                 |  breaking changes:                                                                                                                                                                        |
|                                           |                                                          |  <ul><li>Experimental mode features not available anymore i.e new module does not have the lookup_all_attached_instances module parameter and also does not return attached_instance_information</li><li>New module does not have wait_for_copy and copy_timeout suboptions for source_details module parameter. Waiting till the copy is done, is the default behaviour in the new module.</li></ul>
|                                           |
|oci_volume_backup                          |  oci_blockstorage_volume_backup                          |  breaking changes:                                                                                                                                                                        |
|                                           |                                                          |  <ul><li>New module adds a new module parameter compartment_id and it is required for creating the volume attachment</li></ul>                                                                              |
|                                           |
|oci_volume_backup_actions                  |  oci_blockstorage_volume_backup_actions                  |  no breaking changes                                                                                                                                                                      |
|                                           |
|oci_volume_backup_facts                    |  oci_blockstorage_volume_backup_facts                    |  no breaking changes                                                                                                                                                                      |
|                                           |
|oci_volume_backup_policy_assignment        |  oci_blockstorage_volume_backup_policy_assignment        |  no breaking changes                                                                                                                                                                      |
|                                           |
|oci_volume_backup_policy_assignment_facts  |  oci_blockstorage_volume_backup_policy_assignment_facts  |  no breaking changes                                                                                                                                                                      |
|                                           |
|oci_volume_backup_policy_facts             |  oci_blockstorage_volume_backup_policy_facts             |  no breaking changes                                                                                                                                                                      |
|                                           | 
|oci_volume_facts                           |  oci_blockstorage_volume_facts                           |  breaking changes:                                                                                                                                                                        |
|                                           |                                                          |  <ul><li>Experimental mode features not available anymore i.e new module does not have the lookup_all_attached_instances module parameter and also does not return attached_instance_information</li></ul>  |
|                                           |
|oci_volume_group                           |  oci_blockstorage_volume_group                           |  breaking changes:                                                                                                                                                                        |
|                                           |                                                          |  <ul><li>New module adds the parameter source_details.type and it is required for create.</li></ul>                                                                                                         |
|                                           |
|oci_volume_group_backup                    |  oci_blockstorage_volume_group_backup                    |  breaking changes:                                                                                                                                                                        |
|                                           |                                                          |  <ul><li>compartment_id parameter is required for create in the new module</li></ul>                                                                                                                        |
|                                           |
|oci_volume_group_facts                     |  oci_blockstorage_volume_group_facts                     |  no breaking changes                                                                                                                                                                      |
|                                           |
|oci_volume_group_facts                     |  oci_blockstorage_volume_group_backup_facts              |  no breaking changes                                                                                                                                                                      |


#### Account Management

|old name                     |  new name                     |  migration notes
|-----------------------------|-------------------------------|---------------------
|oci_budget                   |  oci_budget                   |  no breaking changes
|                             |
|oci_budget_alert_rule        |  oci_budget_alert_rule        |  no breaking changes
|                             |
|oci_budget_alert_rule_facts  |  oci_budget_alert_rule_facts  |  no breaking changes
|                             |
|oci_budget_facts             |  oci_budget_facts             |  no breaking changes

#### Audit Management

|old name                       |  new name                       |  migration notes
|-------------------------------|---------------------------------|--------------------------------------------------------------------------------------------------
|                               |                                 |
|oci_audit_configuration        |  oci_audit_configuration        |  no breaking changes
|                               |
|oci_audit_configuration_facts  |  oci_audit_configuration_facts  |  breaking changes:
|                               |                                 |  <ul><li>Return field in new module is configuration resource instead of list of configuration resources.</li></ul>
|                               |
|oci_audit_event_facts          |  oci_audit_event_facts          |  no breaking changes

#### Object Storage

|old name                      |  new name                                     |  migration notes
|------------------------------|-----------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------
|oci_bucket                    |  oci_object_storage_bucket                    |  breaking changes:
|                              |                                               |  <ul><li>`force` parameter is not present anymore, the Objects and Preauthenticated Requests have to be deleted before deleting the bucket</li> <li>update_bucket method is not supported. It is used to move a bucket to a different compartment within the same tenancy</li></ul>
|                              |                                               |  
|oci_bucket_facts              |  oci_object_storage_bucket_facts              |  no breaking change
|                              |
|oci_namespace_facts           |  oci_object_storage_namespace_facts           |  breaking changes:
|                              |                                               |  <ul><li>Return field in new module is namespace instead of namespaces. Also return field type is string instead of list.</li></ul>
|                              |
|oci_namespace_metadata_facts  |  oci_object_storage_namespace_metadata_facts  |  breaking changes:
|                              |                                               |  <ul><li>old repo returns a list of NamespaceMetadata resources, but new repo return just a single one</li></ul>

#### File Storage

|old name                |  new name                             |  migration notes
|------------------------|---------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
|oci_export              |  oci_file_storage_export              |  breaking changes:
|                        |                                       |  <ul><li>New module doesn't support options - 'purge_export_options' & 'delete_export_options'. As a result one can not append/delete specific export option to/from the available list of export options. Please refer the old module documentation for details.</li></ul>
|                        | 
|oci_export_facts        |  oci_file_storage_export_facts        |  no breaking change
|                        |
|oci_export_set          |  oci_file_storage_export_set          |  breaking changes:
|                        |                                       |  <ul><li>New module doesn't map alias 'id' to parameter 'exoprt_set_id'. Alias 'id' is mapped to parameter 'export_id'.</li></ul>
|                        |
|oci_export_set_facts    |  oci_file_storage_export_set_facts    |  no breaking change
|                        |
|oci_file_system         |  oci_file_storage_file_system         |  no breaking change
|                        |
|oci_file_system_facts   |  oci_file_storage_file_system_facts   |  no breaking change
|                        |
|oci_mount_target        |  oci_file_storage_mount_target        |  no breaking change
|                        |
|oci_mount_target_facts  |  oci_file_storage_mount_target_facts  |  no breaking change
|                        |
|oci_snapshot            |  oci_file_storage_snapshot            |  no breaking change
|                        |
|oci_snapshot_facts      |  oci_file_storage_snapshot_facts      |  no breaking change


#### Container Engine

|old name                     |  new name                                    |  migration notes
|-----------------------------|----------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
|                             |                                              |
|oci_cluster                  |  oci_container_engine_cluster                |  breaking changes:
|                             |                                              |  <ul><li>`work_request` is included in the return response of old module, no in the generated one</li></ul>
|                             |
|oci_cluster_facts            |  oci_container_engine_cluster_facts          |  no breaking change
|                             |
|oci_cluster_options_facts    |  oci_container_engine_cluster_options_facts  |  no breaking change
|                             |
|oci_kubeconfig               |  oci_container_engine_kubeconfig             |  breaking changes:
|                             |                                              |  <ul><li>`force` option is not supported in the genereated module, this option was used to overwrite existing kubeconfigs in the old one</li> <li>`dest` option is not supported in the generated module, this option was used to specify the file path to which the kubeconfig content would be written</li> <li>old module would contain the option `create_cluster_kubeconfig_content_details` dict which would have the `expiration` and `token_version` content. old module documentation the new generated module replaces this dict option with it's inner content `expiration` and `token_version`</li> <li>in old repo, we wait for the cluster to become `AVAILABLE` before attempting to create the kubeconfig resource. in new repo, no such wait function is present while creating kubeconfig resource.</li>
|                             |                                              |  
|oci_node_pool                |  oci_container_engine_node_pool              |  breaking changes:
|                             |                                              | <ul><li> `count_of_nodes_to_wait` option is used in old module for providing wait options based on number of nodes in the node_pool.This option is not present in the generated module </li> <li> `lifecycle_details` option is not returned in the generated module</li> <li>return type of option `nodes` is changed from `string` to `complex`</li> <li>`work_request` is included in the return response of old module, no in the generated one</li></ul>
|                             |
|oci_node_pool_facts          |  oci_container_engine_node_pool_facts        |  breaking changes:
|                             |                                              |  <ul><li>return type of `nodes` is changed from `string` to `complex`</li> <li>return type of `cluster_id` is changed from `list` to `string`</li> <li>return type of `initial_node_labels` is changed from `list` to `complex`</li> <li>`lifecycle_details` option is not returned in the generated module</li></ul>
|                             |
|oci_node_pool_options_facts  |  oci_container_engine_node_pool_facts        |  no breaking change