#!/usr/bin/python
# Copyright (c) 2018, 2019 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_load_balancer
short_description: Create, update and delete load balancers in OCI Load Balancing Service
description:
    - Creates OCI Load Balancers
    - Update OCI Load Balancers, if present, with a new display name
    - Delete OCI Load Balancers, if present.
version_added: "2.5"
options:
    compartment_id:
        description: Identifier of the compartment under which this
                     Load Balancer would be created. Mandatory for create
                     operation.Optional for delete and update. Mutually exclusive
                     with C(oci_load_balancer_id).
        required: false
    load_balancer_id:
        description: Identifier of the Load Balancer. Mandatory for delete and update.
        required: false
        aliases: ['id']
    display_name:
        description: Name of the Load Balancer. A user friendly name. Does not have to be unique,
                     and could be changed. Mandatory for create and update.
        required: false
        aliases: ['name']
    state:
        description: Create,update or delete Load Balancer. For I(state=present), if it
                     does not exists, it gets created. If exists, it gets updated.
        required: false
        default: 'present'
        choices: ['present','absent']
    backend_sets:
        description: The configuration details for a load balancer's backend sets
        required: false
        suboptions:
            backends:
               description: A list of configurations related to Backends that are part of a backend set. Each Backend's
                            configuration should be a dict/hash that consist of the following keys
                            ['backup' option specifies whether the load balancer should treat this server as a backup
                            unit. If true, the load balancer forwards no ingress traffic to this backend server unless
                            all other backend servers not marked as "backup" fail the health check policy. required -
                            false],['drain' option specifies whether the load balancer should drain this server. Servers
                            marked "drain" receive no new incoming traffic. required - false], [ip_address describes the
                            IP address of the backend server. required - true], ['offline' ensures whether the load
                            balancer should treat this server as offline. Offline servers receive no incoming traffic.
                            required - false], ['port'  describes the communication port for the backend server.
                            required - true], [ 'weight' describes the load balancing policy weight assigned to the
                            server. Backend servers with a higher weight receive a larger proportion of incoming
                            traffic. For example, a server weighted '3' receives 3 times the number of new connections
                            as a server weighted '1'. required - false]
               required: false
            health_checker:
               description: Describes the health check policy for a backend set. This should be a dict/hash that
                            consists of the following keys
                            ['interval_in_millis' describes the interval between health checks, in milliseconds.
                            required - false], [ 'port' describes the backend server port against which to run the
                            health check. If the port is not specified, the load balancer uses the port information
                            from the backends mentioned above. required - false], ['protocol' describes the protocol
                            the health check must use, either HTTP or TCP. required - true], [ 'response_body_regex'
                            describes a regular expression for parsing the response body from the backend server.
                            required - false], ['retries' describes the number of retries to attempt before a backend
                            server is considered unhealthy. required - false], ['return_code' describes the status code
                            a healthy backend server should return. required - false], ['timeout_in_millis' describes
                            the maximum time, in milliseconds, to wait for a reply to a health check. A health check is
                            successful only if a reply returns within this timeout period. required - false],
                            ['url_path' describes the path against which to run the health check. required - true]
               required: true
            policy:
              description: The load balancer policy for the backend set.
              required: true
            session_persistence_configuration:
              description: The configuration details for implementing session persistence.
                           Session persistence enables the Load Balancing Service to direct any number of requests that
                           originate from a single logical client to a single backend web server. This should be
                           specified as a dict/hash with the following keys
                           ['cookie_name' describes the name of the cookie used to detect a session initiated by the
                           backend server. Use '*' to specify that any cookie set by the backend causes the session to
                           persist. required - true], ['disable_fallback' describes Whether the load balancer is
                           prevented from directing traffic from a persistent session client to a different backend
                           server if the original server is unavailable. Defaults to false. required - false]
              required: false
            ssl_configuration:
              description: The load balancer's SSL handling configuration details. This should be specified as a
                           dict/hash with the following keys
                           [certificate_name describes a friendly name for the certificate bundle. It must be unique
                           and it cannot be changed. Valid certificate bundle names include only alphanumeric
                           characters, dashes, and underscores.Certificate bundle names cannot contain spaces.
                           required - true], ['verify_depth'  describes the maximum depth for peer certificate chain
                           verification. required - false], ['verify_peer_certificate'  describes whether the load
                           balancer listener should verify peer certificates. required - false]
              required: false
    certificates:
        description: The configuration details for a listener certificate bundle.
        suboptions:
            ca_certificate:
               description: The Certificate Authority certificate, or any interim
                            certificate, that you received from your SSL certificate
                            provider.
               required: false
            certificate_name:
               description: A friendly name for the certificate bundle. It must be
                            unique and it cannot be changed. Valid certificate bundle
                            names include only alphanumeric characters, dashes, and
                            underscores. Certificate bundle names cannot contain spaces.
               required: true
            passphrase:
               description: A passphrase for encrypted private keys. This is needed only
                            if you created your certificate with a passphrase.
               required: false
            private_key:
               description: The SSL private key for your certificate, in PEM format.
               required: false
            public_certificate:
               description: The public certificate, in PEM format, that you received
                            from your SSL certificate provider.
               required: false
        required: false
    is_private:
        description: Defines whether the load balancer has a VCN-local (private) IP address.
        required: false
        type: bool
    listeners:
        description: The listener configuration details.
        suboptions:
            default_backend_set_name:
               description: The name of the associated backend set.
               required: true
            port:
               description: The communication port for the listener.
               required: true
            protocol:
               description: The protocol on which the listener accepts connection requests.
               required: true
            ssl_configuration:
               description: The load balancer SSL handling configuration details. Consists of
                            following options, ['certificate_name' describes a friendly name for
                            the certificate bundle. It must be unique and it cannot be changed.
                            Valid certificate bundle names include only alphanumeric characters,
                            dashes, and underscores.Certificate bundle names cannot contain spaces.
                            required - true],['verify_depth'  describes the maximum depth for peer
                            certificate chain verification. required - false], ['verify_peer_certificate'
                            describes whether the load balancer listener should verify peer certificates.
                            required - false]
               required: false
            connection_configuration:
               description: Configuration details for the connection between the client and backend servers.
                            Consists of following options, ['idle_timeout' describes The maximum idle time,
                            in seconds, allowed between two successive receive or two successive send operations
                            between the client and backend servers. A send operation does not reset the timer
                            for receive operations. A receive operation does not reset the timer for send operations.]
               required: false
            hostname_names:
                description: An array of hostname resource names.
                required: false
            path_route_set_name:
                description: The name of the set of path-based routing rules, PathRouteSet, applied to this listener's traffic.
                required: false
        required: false
    path_route_sets:
        description: The configuration details for a load balancer's path route sets
        required: false
        suboptions:
            path_routes:
               description: A list of configurations related to Path Routes that are part of a path route set.
                            Each Path Route's configuration should be a dict/hash that consist of the following keys
                            ['backend_set_name' option specifies The name of the target backend set for requests where
                            the incoming URI matches the specified path.required - true],['path' option specifies the
                            path string to match against the incoming URI path. required - true], ['path_match_type'
                            describes the type of matching to apply to incoming URIs.The value of this attribute is another
                            dict/hash with 'match_type' is key and value is one of EXACT_MATCH, FORCE_LONGEST_PREFIX_MATCH,
                            PREFIX_MATCH, SUFFIX_MATCH. required - true]
    hostnames:
        description: The details of a hostname resource associated with a load balancer.
        suboptions:
            hostname:
               description: A virtual hostname.
               required: true
            name:
               description: The name of the hostname resource.
               required: true
    shape_name:
        description: A template that determines the total pre-provisioned bandwidth (ingress plus egress).
        required: true
    subnet_ids:
        description: An array of subnet OCIDs.
        required: true
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: [ oracle, oracle_creatable_resource, oracle_wait_options ]
"""

EXAMPLES = """
# Note: These examples do not set authentication details.
# Create Load Balancer
- name: Create Load Balancer
  oci_load_balancer:
    compartment_id: "ocid1.compartment.xvds"
    name: "ansible_lb"
    backend_sets:
     backend1:
      backends:
          - ip_address: "10.159.34.21"
            port: "8080"
      health_checker:
          interval_in_millis: "30000"
          port: "8080"
          protocol: "HTTP"
          response_body_regex: "^(500|40[1348])$"
          retries: "3"
          timeout_in_millis: "6000"
          return_code: "200"
          url_path: "/healthcheck"
      policy: "LEAST_CONNECTIONS"
    shape_name: "100Mbps"
    listeners:
      listerner1:
        default_backend_set_name: "backend1"
        port: "80"
        protocol: "HTTP"
        hostname_names: ['hostname_001']
        path_route_set_name: 'test_path_route_set'
    subnet_ids:
        - "ocid1.subnet.ad1"
        - "ocid1.subnet.ad2"
    certificates:
        certs1:
            ca_certificate: "fullchain.pem"
            private_key: "privkey.pem"
            public_certificate: "ca_cert.pem"
            certificate_name: "certs1"
    path_route_sets:
          test_path_route_set:
              path_routes:
                  - backend_set_name: "backend1"
                    path: "/admin"
                    path_match_type:
                       match_type: 'EXACT_MATCH'
    hostnames:
       ansible_hostname:
           name: 'ansible_hostname'
           hostname: 'myapp.example.com'
    state: 'present'
# Update Load Balancer
- name: Update Load Balancer
  oci_load_balancer:
    load_balancer_id: "ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx"
    name: "ansible_lb_updated"
    state: 'present'
# Deleted Load Balancer
- name: Update Load Balancer
  oci_load_balancer:
    load_balancer_id: "ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx"
    state: 'absent'
"""

RETURN = """
    load_balancer:
        description: Attributes of the created/updated Load Balancer.
                    For delete, deleted Load Balancer description will
                    be returned.
        returned: success
        type: complex
        contains:
            compartment_id:
                description: The identifier of the compartment containing the Load Balancer
                returned: always
                type: string
                sample: ocid1.compartment.oc1.xzvf..oifds
            display_name:
                description: Name assigned to the Load Balancer during creation
                returned: always
                type: string
                sample: ansible_lb
            id:
                description: Identifier of the Load Balancer
                returned: always
                type: string
                sample: ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx
            lifecycle_state:
                description: The current state of the Load Balancer
                returned: always
                type: string
                sample: ACTIVE
            time_created:
                description: Date and time when the Load Balancer was created, in
                             the format defined by RFC3339
                returned: always
                type: datetime
                sample: 2016-08-25T21:10:29.600Z
            backend_sets:
                description: The configuration details for a load balancer backend set
                returned: always
                type: dict
                sample: {"backend1": {"backends": [{"backup": false, "drain": false,
                        "ip_address": "10.159.34.21", "name": "10.159.34.21:8080",
                        "offline": false, "port": 8080, "weight": 1}],
                        "health_checker": {"interval_in_millis": 30000, "port": 8080,
                        "protocol": "HTTP", "response_body_regex": "^(500|40[1348])$",
                        "retries": 3, "return_code": 200, "timeout_in_millis": 6000,
                        "url_path": "/healthcheck", "name": "backend1",
                        "policy": "LEAST_CONNECTIONS", "session_persistence_configuration": null,
                        "ssl_configuration": null}}}
            certificates:
                description: The configuration details for a listener certificate bundle.
                returned: always
                type: dict
                sample: {"certs1": {"ca_certificate": "-----BEGIN CERTIFICATE-----\\nMIIFKTCCBBGgAwIBAgISBIs5aiZ1fWapuAl2P9POFMXjMA0GCSqGSIb3DQEBCwUA\\n
                            -----END CERTIFICATE-----\\n-----BEGIN CERTIFICATE-----\\n-----END CERTIFICATE-----", "certificate_name": "certs1",
                            "public_certificate":"-----BEGIN CERTIFICATE-----\\nMIIFKTCCBBGgAwIBAgISBIs5aiZ1fWapuAl2P9POFMXjMA0GCSqGSIb3DQEBCwUA\\n
                            -----END CERTIFICATE-----"}}
            listeners:
                description: The listener configuration details.
                returned: always
                type: dict
                sample: {"listerner1": {"default_backend_set_name": "backend1", "name": "listerner1",
                         "port": 80, "protocol": "HTTP", "ssl_configuration": null, "connection_configuration":{"idle_timeout": 1200}}}
            path_route_sets:
                description: The path route sets configuration details.
                returned: always
                type: dict
            sample: {
                      "ansible_path_route_set":{
                      "path_routes":[
                                     {
                                       "backend_set_name":"ansible_backend_set",
                                       "path":"/example/user",
                                       "path_match_type":{
                                             "match_type":"EXACT_MATCH"
                                     }
                                   }
                                  ]
                                 }
                    }
            shape_name:
                description: A template that determines the total pre-provisioned bandwidth (ingress plus egress).
                returned: always
                type: string
                sample: 100Mbps
            hostnames:
                description: The details of a hostname resource associated with a load balancer.
                returned: always
                type: dict
                sample: {
                         "ansible_hostname": {
                             "name": "ansible_hostname",
                             "hostname": "app.example.com"
                           }
                         }
            subnet_ids:
                description: An array of subnet OCIDs.
                returned: always
                type: list
                sample: ["ocid1.subnet.oc1.iad.xxxxxEXAMPLExxxxx",
                    "ocid1.subnet.oc1.iad.xxxxxEXAMPLExxxxx"]
        sample: {
   "backend_sets":{
      "backend1":{
         "backends":[
            {
               "backup":false,
               "drain":false,
               "ip_address":"10.159.34.21",
               "name":"10.159.34.21:8080",
               "offline":false,
               "port":8080,
               "weight":1
            }
         ],
         "health_checker":{
            "interval_in_millis":30000,
            "port":8080,
            "protocol":"HTTP",
            "response_body_regex":"^(500|40[1348])$",
            "retries":3,
            "return_code":200,
            "timeout_in_millis":6000,
            "url_path":"/healthcheck"
         },
         "name":"backend1",
         "policy":"LEAST_CONNECTIONS",
         "session_persistence_configuration":null,
         "ssl_configuration":null
      }
   },
   "certificates":{
      "certs1":{
         "ca_certificate":"-----BEGIN CERTIFICATE-----\\nMIIFKTCCBBGgAwIBAgISBIs5aiZ1fWapuAl2P9POFMXjMA0GCSqGSIb3DQEBCwUA\\n-----END CERTIFICATE
                          -----\\n-----BEGIN CERTIFICATE-----\\n-----END CERTIFICATE-----",
         "certificate_name":"certs1",
         "public_certificate":"-----BEGIN CERTIFICATE-----\\nMIIFKTCCBBGgAwIBAgISBIs5aiZ1fWapuAl2P9POFMXjMA0GCSqGSIb3DQEBCwUA\\n-
                              ----END CERTIFICATE-----"
      }
   },
   "path_route_sets":{
                      "ansible_path_route_set":{
                      "path_routes":[
                                     {
                                       "backend_set_name":"ansible_backend_set",
                                       "path":"/example/user",
                                       "path_match_type":{
                                             "match_type":"EXACT_MATCH"
                                     }
                                   }
                                  ]
                                 }
                    },
   "compartment_id":"ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
   "display_name":"ansible_lb955",
   "id":"ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx",
   "ip_addresses":[
      {
         "ip_address":"129.213.72.32",
         "is_public":true
      }
   ],
   "is_private": false,
   "lifecycle_state":"ACTIVE",
   "listeners":{
      "listerner1":{
         "default_backend_set_name":"backend1",
         "name":"listerner1",
         "port":80,
         "protocol":"HTTP",
         "ssl_configuration":null,
         "connection_configuration": {
             "idle_timeout": 1200
          }
      }
   },
   "hostnames":{
       "ansible_hostname": {
                             "name": "ansible_hostname",
                             "hostname": "app.example.com"
                           }
   },
   "shape_name":"100Mbps",
   "subnet_ids":[
      "ocid1.subnet.oc1.iad.xxxxxEXAMPLExxxxx",
      "ocid1.subnet.oc1.iad.xxxxxEXAMPLExxxxx"
   ],
   "time_created":"2018-01-06T18:22:17.198000+00:00"
}
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils, oci_lb_utils
from ansible.module_utils import six

try:
    import copy
    from oci.load_balancer.load_balancer_client import LoadBalancerClient
    from oci.exceptions import ServiceError, ClientError
    from oci.util import to_dict
    from oci.load_balancer.models import (
        CreateLoadBalancerDetails,
        UpdateLoadBalancerDetails,
    )

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False

logger = None


def create_or_update_lb(lb_client, module):
    result = dict(changed=False, load_balancer="")
    load_balancer_id = module.params.get("load_balancer_id")
    default_attribute_values = {
        "backend_sets": {
            "backends": {
                "backup": False,
                "drain": False,
                "offline": False,
                "weight": 1,
            },
            "health_checker": {
                "interval_in_millis": 10000,
                "port": 0,
                "response_body_regex": ".*",
                "retries": 3,
                "return_code": 200,
                "timeout_in_millis": 3000,
            },
        },
        "listeners": {
            "connection_configuration": {"idle_timeout": 60},
            "rule_set_names": [],
        },
    }
    exclude_attributes = {"display_name": True}

    try:
        if load_balancer_id:
            existing_load_balancer = oci_utils.get_existing_resource(
                lb_client.get_load_balancer, module, load_balancer_id=load_balancer_id
            )
            result = update_load_balancer(lb_client, module, existing_load_balancer)
        else:
            module1 = copy.deepcopy(module)
            module1.params.update(
                {
                    "certificates": to_dict(
                        oci_lb_utils.create_certificates(
                            module1.params.get("certificates")
                        )
                    )
                }
            )
            result = oci_utils.check_and_create_resource(
                resource_type="load_balancer",
                create_fn=create_load_balancer,
                kwargs_create={"lb_client": lb_client, "module": module},
                list_fn=lb_client.list_load_balancers,
                kwargs_list={"compartment_id": module.params.get("compartment_id")},
                module=module1,
                exclude_attributes=exclude_attributes,
                default_attribute_values=default_attribute_values,
                model=CreateLoadBalancerDetails(),
            )
    except ServiceError as ex:
        get_logger().error(
            "Unable to create/update load balancer due to: %s", ex.message
        )
        module.fail_json(msg=ex.message)
    except ClientError as ex:
        get_logger().error("Unable to create/update backend due to: %s", str(ex))
        module.fail_json(msg=str(ex))

    return result


def create_load_balancer(lb_client, module):
    compartment_id = module.params["compartment_id"]
    name = module.params["display_name"]
    get_logger().info(
        "Creating load balancer %s in the compartment %s", name, compartment_id
    )
    backend_sets = oci_lb_utils.create_backend_sets(
        module.params.get("backend_sets", None)
    )
    certificates = oci_lb_utils.create_certificates(
        module.params.get("certificates", None)
    )
    listeners = oci_lb_utils.create_listeners(module.params.get("listeners", None))
    path_route_sets = oci_lb_utils.create_path_route_sets(
        module.params.get("path_route_sets", None)
    )
    hostnames = oci_lb_utils.create_hostnames(module.params.get("hostnames", None))
    subnet_ids = module.params["subnet_ids"]
    shape_name = module.params["shape_name"]
    is_private = module.params.get("is_private", False)
    create_load_balancer_details = CreateLoadBalancerDetails()
    atributes_to_value_dict = dict(
        {
            "compartment_id": compartment_id,
            "display_name": name,
            "is_private": is_private,
            "certificates": certificates,
            "listeners": listeners,
            "backend_sets": backend_sets,
            "path_route_sets": path_route_sets,
            "hostnames": hostnames,
            "shape_name": shape_name,
            "subnet_ids": subnet_ids,
        }
    )
    for key, value in six.iteritems(atributes_to_value_dict):
        create_load_balancer_details.__setattr__(key, value)
    return oci_lb_utils.create_or_update_lb_resources_and_wait(
        resource_type="load_balancer",
        function=lb_client.create_load_balancer,
        kwargs_function={"create_load_balancer_details": create_load_balancer_details},
        lb_client=lb_client,
        get_fn=lb_client.get_load_balancer,
        get_param="load_balancer_id",
        module=module,
    )


def update_load_balancer(lb_client, module, load_balancer):
    if load_balancer is None:
        raise ClientError(
            Exception(
                "No Load Balancer with id "
                + module.params.get("load_balancer_id")
                + " is found for update"
            )
        )
    result = dict(load_balancer=to_dict(load_balancer), changed=False)
    name = module.params["display_name"]
    update_load_balancer_details = UpdateLoadBalancerDetails()
    if load_balancer.display_name.strip() != name.strip():
        get_logger().info(
            "Updating the display name of load balancer from %s to %s",
            load_balancer.display_name,
            name,
        )
        update_load_balancer_details.display_name = name
        result = oci_lb_utils.create_or_update_lb_resources_and_wait(
            resource_type="load_balancer",
            function=lb_client.update_load_balancer,
            kwargs_function={
                "update_load_balancer_details": update_load_balancer_details,
                "load_balancer_id": load_balancer.id,
            },
            lb_client=lb_client,
            get_fn=lb_client.get_load_balancer,
            kwargs_get={"load_balancer_id": load_balancer.id},
            module=module,
        )

        get_logger().info(
            "Successfully updated the display name of load balancer from %s to %s",
            load_balancer.display_name,
            name,
        )
    if not result["changed"]:
        get_logger().info(
            "Unable to update display name of load balancer as the new name is same as old"
        )
    return result


def delete_load_balancer(lb_client, module):
    lb_id = module.params.get("load_balancer_id")
    get_logger().info("Deleting load balancer %s", lb_id)
    result = oci_lb_utils.delete_lb_resources_and_wait(
        resource_type="load_balancer",
        function=lb_client.delete_load_balancer,
        kwargs_function={"load_balancer_id": lb_id},
        lb_client=lb_client,
        get_fn=lb_client.get_load_balancer,
        kwargs_get={"load_balancer_id": lb_id},
        module=module,
    )
    if result["changed"]:
        get_logger().info("Successfully deleted load balancer %s", lb_id)
    else:
        get_logger().info("Load balancer %s is already deleted", lb_id)

    return result


def set_logger(input_logger):
    global logger
    logger = input_logger


def get_logger():
    return logger


def main():
    logger = oci_utils.get_logger("oci_load_balancer")
    set_logger(logger)
    module_args = oci_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=False),
            display_name=dict(type="str", required=False, aliases=["name"]),
            load_balancer_id=dict(type="str", required=False, aliases=["id"]),
            backend_sets=dict(type=dict, required=False),
            certificates=dict(type=dict, required=False),
            listeners=dict(type=dict, required=False),
            hostnames=dict(type=dict, required=False),
            shape_name=dict(type="str", required=False),
            subnet_ids=dict(type=list, required=False),
            path_route_sets=dict(type=dict, required=False),
            state=dict(
                type="str",
                required=False,
                default="present",
                choices=["present", "absent"],
            ),
            is_private=dict(type="bool", required=False, default=False),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        mutually_exclusive=[["compartment_id", "load_balancer_id"]],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    lb_client = oci_utils.create_service_client(module, LoadBalancerClient)
    state = module.params["state"]

    if state == "present":
        result = create_or_update_lb(lb_client, module)
    elif state == "absent":
        result = delete_load_balancer(lb_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
