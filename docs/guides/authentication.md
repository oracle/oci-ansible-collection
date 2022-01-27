# Authentication Guide

OCI Ansible supports the following authentication mechanisms:

- [API Key](#api-key-authentication)
- [Instance Principal](#instance-principal)
- [Delegation Auth](#delegation-auth)
- [Resource Principal](#resource-principal)

The *default* option is api_key.



## API Key Authentication

- Use api key of the user. [Read more](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm).
- Having a [CLI config file](#sdk-and-cli-configuration) is mandatory for api_key.
- However, parameters in the config file can be customized using environment variables or module options.

- For example, to fetch VCNs in a compartment, the below task uses auth type as api_key  
  and overrides the region parameter (if say the config file pointed to some other region):

``` yaml
- name: List vcns
  oci_network_vcn_facts:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    region: "us-ashburn-1"
```

## Instance Principal

- Use authentication credentials of the compute instance. [Read more](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/callingservicesfrominstances.htm).

- For example, similar to the *fetch VCNs in a compartment* example above,  
  via auth type as instance principal, can be achieved like this:

``` yaml
- name: List vcns
  oci_network_vcn_facts:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    auth_type: "instance_principal"
    region: "us-ashburn-1"
```


## Delegation Auth

- Can be used when running via cloud shell. [Read more](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/cloudshellgettingstarted.htm).

``` yaml
- name: List vcns
  oci_network_vcn_facts:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    auth_type: "instance_obo_user"
    region: "us-ashburn-1"
```


## Resource Principal

- Very similar to instance principal auth but used for resources  
  that are not instances, such as serverless functions.

``` yaml
- name: List vcns
  oci_network_vcn_facts:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    auth_type: "resource_principal"
    region: "us-ashburn-1"
```



## Parameters

The following parameters need to be set when one of the above authentication mechanism is chosen.

### AUTH TYPE

    Description:                          Choose one of the authentication mechanisms listed above.

    Type:                                 String

    Default:                              api_key

    Configuration Mechanisms:

            Environment Variable:         OCI_ANSIBLE_AUTH_TYPE

            Module Option:                auth_type

    Options:                              [api_key, instance_obo_user, instance_principal, resource_principal]



### TENANCY

    Description:                          OCID of your tenancy.

    Type:                                 String

    Configuration Mechanisms:

            Environment Variable:         OCI_TENANCY

            Module Option:                tenancy

            SDK and CLI Configuration     tenancy

    Used:                                 When auth_type is api_key (required)



### REGION

    Description:                          The Oracle Cloud Infrastructure region to use for all OCI API requests.

    Type:                                 String

    Configuration Mechanisms:

            Environment Variable:         OCI_REGION

            Module Option:                region

            SDK and CLI Configuration     region

    Used:                                 When auth_type is api_key (required)



### API USER

    Description:                          The OCID of the user, on whose behalf, OCI APIs are invoked.

    Type:                                 String

    Configuration Mechanisms:

            Environment Variable:         OCI_USER_ID

            Module Option:                api_user

            SDK and CLI Configuration     user

    Used:                                 When auth_type is api_key (required)



### API USER FINGERPRINT

    Description:                          Fingerprint for the key pair being used

    Type:                                 String

    Configuration Mechanisms:

            Environment Variable:         OCI_USER_FINGERPRINT

            Module Option:                api_user_fingerprint

            SDK and CLI Configuration     fingerprint

    Used:                                 When auth_type is api_key (required)



### API USER KEY FILE
    Description:                          Full path and filename of the private key (in PEM format)

    Type:                                 String

    Configuration Mechanisms:

            Environment Variable:         OCI_USER_KEY_FILE

            Module Option:                api_user_key_file

            SDK and CLI Configuration     key_file

    Used:                                 When auth_type is api_key (required)



### API USER KEY PASSPHRASE

    Description:                          Passphrase used by the key referenced in api_user_key_file, if it is encrypted

    Type:                                 String

    Configuration Mechanisms:

            Environment Variable:         OCI_USER_KEY_PASS_PHRASE

            Module Option:                api_user_key_pass_phrase

            SDK and CLI Configuration     pass_phrase

    Used:                                 When auth_type is api_key (optional)



## Module Options Example

Ansible module option auth_type can be set to configure the authentication type,
for example, to fetch VCNs in a compartment, we can pass the authentication as below:


``` yaml
- name: List vcns
  oci_network_vcn_facts:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    auth_type: "instance_principal"
```


When auth_type is api_key, tenancy, region and other variables can also be set via module options as below:

``` yaml
- name: List vcns
  oci_network_vcn_facts:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    tenancy: "your_tenancy"
    region: "your_oci_region"
    api_user: "api_user"
    api_user_fingerprint: "api_user_fingerprint"
    api_user_key_file: "api_user_key_file"
    api_user_key_pass_phrase: "api_user_key_pass_phrase"
```


## SDK and CLI Configuration

- SDK configuration files can be used to specify authentication information.
- To support multiple users, use the "profiles" feature in the SDK configuration file.
  [Read more](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm).

- The config file location and config profile name can be passed to the ansible module via:

      Environment Variables
        - OCI_CONFIG_FILE
        - OCI_CONFIG_PROFILE  
      Module Options:
        - config_file_location
        - config_profile_name

- When neither the module option is used nor the environment variable,  
  Config file location defaults to ```~/.oci/config```

- When neither the module option is used nor the environment variable,  
  Config profile name defaults to the ```DEFAULT``` profile in the config file


## Precedence

The following is the precedence order for the configs:

- Module Options
- Environment Variables
- SDK and CLI Configuration file parameters
