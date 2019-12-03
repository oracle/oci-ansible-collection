#!/usr/bin/python
# Copyright (c) 2018, 2019, Oracle and/or its affiliates.
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
module: oci_load_balancer_facts
short_description: Fetches details of the OCI Load Balancer
description:
    - Fetches details of the OCI Load Balancer.
version_added: "2.5"
options:
    compartment_id:
        description: Identifier of the compartment in which this
                     Load Balancer exists
        required: false
    load_balancer_id:
        description: Identifier of the Load Balancer whose details needs to be fetched.
        required: false
        aliases: ['id']
    detail:
        description: The level of detail to return for each result.
        choices: ['full', 'simple']
        required: false
    lifecycle_state:
        description: A filter to return only resources that match the given lifecycle state.
        required: false
        choices: ["CREATING", "FAILED", "ACTIVE", "DELETING", "DELETED"]
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: [ oracle, oracle_display_name_option ]
"""

EXAMPLES = """
#Fetch Load Balancer
- name: List Load Balancer
  oci_load_balancer_facts:
      compartment_id: 'ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx'

#Fetch specific Load Balancer
- name: List a specific Load Balancer
  oci_load_balancer_facts:
      load_balancer_id: 'ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx'
"""

RETURN = """
    load_balancers:
        description: Attributes of the  Load Balancers.
        returned: success
        type: complex
        contains:
            compartment_id:
                description: The identifier of the compartment containing the Load Balancer
                returned: always
                type: string
                sample: ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx
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
                            "public_certificate":"-----BEGIN CERTIFICATE-----\nMIIFKTCCBBGgAwIBAgISBIs5aiZ1fWapuAl2P9POFMXjMA0GCSqGSIb3DQEBCwUA\\n
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
            subnet_ids:
                description: An array of subnet OCIDs.
                returned: always
                type: list
                sample: ["ocid1.subnet.oc1.iad.xxxxxEXAMPLExxxxx", "ocid1.subnet.oc1.iad.xxxxxEXAMPLExxxxx"]
        sample: [{
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
   "is_private":false,
   "lifecycle_state":"ACTIVE",
   "listeners":{
      "listener1":{
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
   "shape_name":"100Mbps",
   "subnet_ids":[
      "ocid1.subnet.oc1.iad.xxxxxEXAMPLExxxxx",
      "ocid1.subnet.oc1.iad.xxxxxEXAMPLExxxxx"
   ],
   "time_created":"2018-01-06T18:22:17.198000+00:00"
}]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.load_balancer.load_balancer_client import LoadBalancerClient
    from oci.exceptions import ServiceError
    from oci.util import to_dict

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False

logger = None


def list_load_balancers(lb_client, module):
    result = dict(load_balancers="")
    compartment_id = module.params.get("compartment_id")
    load_balancer_id = module.params.get("load_balancer_id")
    try:
        if compartment_id:
            get_logger().debug(
                "Listing all load balancers under compartment %s", compartment_id
            )
            optional_list_method_params = ["display_name", "detail", "lifecycle_state"]
            optional_kwargs = dict(
                (param, module.params[param])
                for param in optional_list_method_params
                if module.params.get(param) is not None
            )
            existing_load_balancers = oci_utils.list_all_resources(
                lb_client.list_load_balancers,
                compartment_id=compartment_id,
                **optional_kwargs
            )
        elif load_balancer_id:
            get_logger().debug("Listing load balancer %s", load_balancer_id)
            response = lb_client.get_load_balancer(load_balancer_id)
            existing_load_balancers = [response.data]
    except ServiceError as ex:
        get_logger().error("Unable to list load balancers due to %s", ex.message)
        module.fail_json(msg=ex.message)
    result["load_balancers"] = to_dict(existing_load_balancers)
    return result


def set_logger(input_logger):
    global logger
    logger = input_logger


def get_logger():
    return logger


def main():
    logger = oci_utils.get_logger("oci_load_balancer_facts")
    set_logger(logger)
    module_args = oci_utils.get_facts_module_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=False),
            load_balancer_id=dict(type="str", required=False, aliases=["id"]),
            lifecycle_state=dict(
                type="str",
                required=False,
                choices=["CREATING", "FAILED", "ACTIVE", "DELETING", "DELETED"],
            ),
            detail=dict(type=str, required=False, choices=["full", "simple"]),
        )
    )
    module = AnsibleModule(
        argument_spec=module_args,
        mutually_exclusive=[["compartment_id", "load_balancer_id"]],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    lb_client = oci_utils.create_service_client(module, LoadBalancerClient)
    result = list_load_balancers(lb_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
