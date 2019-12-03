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
module: oci_load_balancer_backend_set
short_description: Create, update and delete a backend set of a load balancer.
description:
    - Create an OCI Load Balancer Backend Set
    - Update OCI Load Balancers Backend Set, if present.
    - Delete OCI Load Balancers Backend Set, if present.
version_added: "2.5"
options:
    load_balancer_id:
        description: Identifier of the Load Balancer. Mandatory for create,delete and update.
        required: true
        aliases: ['id']
    name:
        description: Name of the Load Balancer Backend Set. A user friendly name. Does not have to be unique,
                     and could be changed. Mandatory for create and update.
        required: false
    state:
        description: Create,update or delete Load Balancer Backend Set. For I(state=present), if it
                     does not exists, it gets created. If exists, it gets updated.
        required: false
        default: 'present'
        choices: ['present','absent']
    policy:
        description: The load balancer policy for the backend set. M(oci_load_balancer_policy_facts) could be
                     used to fetch policy types suupported by OCI Load Balancer Service.
        required: false
    backends:
        description: A list of configurations related to Backends that are part of a backend set.
        required: false
        suboptions:
           ip_address:
              description: IP address of the backend server.
              required: true
           port:
              description: The communication port for the backend server
              required: true
           backup:
              description: Specifies whether the load balancer should treat this server as a backup
                           unit. If true, the load balancer forwards no ingress traffic to this backend
                           server unless all other backend servers not marked as "backup" fail the health
                           check policy.
              required: false
              default: False
           drain:
              description: Specifies whether the load balancer should drain this server. Servers
                           marked "drain" receive no new incoming traffic.
              required: false
              default: False
           offline:
              description: Ensures whether the load balancer should treat this server as offline.
                           Offline servers receive no incoming traffic.
              required: false
              default: False
           weight:
              description: Describes the load balancing policy weight assigned to the server.
                           Backend servers with a higher weight receive a larger proportion of incoming
                           traffic. For example, a server weighted '3' receives 3 times the number of new
                           connections as a server weighted '1'.
              required: false
              default: 1
    health_checker:
        description: Describes the health check policy for a backend set.
        required: false
        suboptions:
            interval_in_millis:
              description: Describes the interval between health checks, in milliseconds.
              required: false
              default: 10000
            port:
              description: Describes the backend server port against which to run the
                           health check. If the port is not specified, the load balancer
                           uses the port information from the backends.
              required: false
              default: 0
            protocol:
              description: Describes the protocol the health check must use, either HTTP or TCP.
              required: true
              choices: ['HTTP', 'TCP']
            response_body_regex:
              description: Describes a regular expression for parsing the response body from the
                           backend server.
              required: false
              default: '.*'
            retries:
              description: Describes the number of retries to attempt before a backend
                           server is considered unhealthy.
              required: false
              default: 3
            return_code:
              description: Describes the status code a healthy backend server should return.
              required: false
              default: 200
            timeout_in_millis:
              description: Describes the maximum time, in milliseconds, to wait for a reply to
                           a health check. A health check is successful only if a reply returns
                           within this timeout period.
              required: false
              default: 3000
            url_path:
              description: Describes the path against which to run the health check.
              required: true
    session_persistence_configuration:
        description: The configuration details for implementing session persistence. Session
                     persistence enables the Load Balancing Service to direct any number of
                     requests that originate from a single logical client to a single backend
                     web server.
        required: false
        suboptions:
            cookie_name:
              description: Describes the name of the cookie used to detect a session initiated by the
                           backend server. Use '*' to specify that any cookie set by the backend causes
                           the session to persist.
              required: true
            disable_fallback:
              description: DescribesWhether the load balancer is prevented from directing traffic from a
                           persistent session client to a different backend server if the original server
                           is unavailable.
              required: false
              default: False
    ssl_configuration:
        description: The load balancer's SSL handling configuration details.
        required: false
        suboptions:
            certificate_name:
              description: Describes a friendly name for the certificate bundle. It must be unique
                           and it cannot be changed. Valid certificate bundle names include only alphanumeric
                           characters, dashes, and underscores.Certificate bundle names cannot contain spaces.
              required: true
            verify_depth:
              description: Describes the maximum depth for peer certificate chain verification.
              required: false
            verify_peer_certificate:
              description: Describeswhether the load balancer listener should verify peer certificates.
              required: false
    purge_backends:
        description: Purge any backends in the  Backend Set named I(name) that is not specified in I(backends).
                     If I(purge_backends=no), provided backends would be appended to existing backends.
                     I(purge_backends) and I(delete_backends) are mutually exclusive.
        required: false
        default: 'yes'
        type: bool
    delete_backends:
        description: Delete any backends in the  Backend Set named I(name) that is specified in I(backends).
                     If I(delete_backends=yes), backends provided by I(backends) would be deleted from existing
                     backends, if they are part of existing backends. If they are not part of existing backends,
                     they will be ignored. I(delete_backends) and I(purge_backends) are mutually exclusive.
        required: false
        default: 'no'
        type: bool
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: [ oracle, oracle_wait_options ]
"""

EXAMPLES = """
# Note: These examples do not set authentication details.
# Create Create a backend set named "ansible_backend_set" in a load balancer
- name: Create Load Balancer Backend Set
  oci_load_balancer_backend_set:
    name: "ansible_backend_set"
    load_balancer_id: "ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx"
    backends:
          - ip_address: "10.159.34.21"
            port: 8080
    health_checker:
          interval_in_millis: 30000
          port: 8080
          protocol: "HTTP"
          response_body_regex: "^(500|40[1348])$"
          retries: 3
          timeout_in_millis: 6000
          return_code: 200
          url_path: "/healthcheck"
    policy: "LEAST_CONNECTIONS"
    session_persistence_configuration:
      cookie_name: "ansible_backend_set_cookie"
      disable_fallback: True
    ssl_configuration:
      certificate_name: "certs1"
      verify_depth: 3
      verify_peer_certificate: True
    state: 'present'

# Update Load Balancer Backend Set
- name: Update Load Balancer Backend Set
  oci_load_balancer_backend_set:
    load_balancer_id: "ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx"
    name: "ansible_backend_set"
    backends:
          - ip_address: "10.159.34.25"
            port: 8282
    purge_backends: 'no'
    state: 'present'

# Update Load Balancer Backend Set by deleting backends
- name: Update Load Balancer Backend Set by deleting backends
  oci_load_balancer_backend_set:
    load_balancer_id: "ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx"
    name: "ansible_backend_set"
    backends:
          - ip_address: "10.159.34.25"
            port: 8282
    delete_backends: 'yes'
    state: 'present'

# Deleted Load Balancer Backend Set
- name: Update Load Balancer Backend Set
  oci_load_balancer_backend_set:
    load_balancer_id: "ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx"
    name: "ansible_backend_set"
    state: 'absent'
"""

RETURN = """
    backend_set:
        description: Attributes of the created/updated Load Balancer Backend Set.
                    For delete, deleted Load Balancer Backend Set description will
                    be returned.
        returned: success
        type: complex
        contains:
            backends:
                description: A list of configurations related to Backends that are part of the backend set
                returned: always
                type: list
                sample: [
                            {
                                "backup": false,
                                "drain": false,
                                "ip_address": "10.159.34.21",
                                "name": "10.159.34.21:8080",
                                "offline": false,
                                "port": 8080,
                                "weight": 1
                            },
                            {
                                "backup": false,
                                "drain": false,
                                "ip_address": "10.159.34.21",
                                "name": "10.159.34.21:8282",
                                "offline": false,
                                "port": 8282,
                                "weight": 1
                            }
                        ]
            name:
                description: Name assigned to the Load Balancer Backend Set during creation
                returned: always
                type: string
                sample: ansible_backend_set
            health_checker:
                description: Health check policy for a backend set.
                returned: always
                type: dict
                sample: {
                            "interval_in_millis": 30000,
                            "port": 8080,
                            "protocol": "HTTP",
                            "response_body_regex": "^(500|40[1348])$",
                            "retries": 3,
                            "return_code": 200,
                            "timeout_in_millis": 6000,
                            "url_path": "/healthcheck"
                        }
            policy:
                description: The load balancer policy for the backend set.
                returned: always
                type: string
                sample: LEAST_CONNECTIONS
            session_persistence_configuration:
                description: The configuration details for implementing session persistence
                returned: always
                type: dict
                sample: {
                            "cookie_name": "first_backend_set_cookie",
                            "disable_fallback": true
                        }
            ssl_configuration:
                description: The load balancer's SSL handling configuration details.
                returned: always
                type: dict
                sample: {
                            "certificate_name": "certs1",
                            "verify_depth": 1,
                            "verify_peer_certificate": true
                        }
        sample: {"backends": [
            {
                "backup": false,
                "drain": false,
                "ip_address": "10.159.34.21",
                "name": "10.159.34.21:8080",
                "offline": false,
                "port": 8080,
                "weight": 1
            },
            {
                "backup": false,
                "drain": false,
                "ip_address": "10.159.34.21",
                "name": "10.159.34.21:8282",
                "offline": false,
                "port": 8282,
                "weight": 1
            }
        ],
        "health_checker": {
            "interval_in_millis": 30000,
            "port": 8080,
            "protocol": "HTTP",
            "response_body_regex": "^(500|40[1348])$",
            "retries": 3,
            "return_code": 500,
            "timeout_in_millis": 6000,
            "url_path": "/healthcheck"
        },
        "name": "backend_set_1",
        "policy": "IP_HASH",
        "session_persistence_configuration": {
            "cookie_name": "first_backend_set_cookie_updated",
            "disable_fallback": true
        },
        "ssl_configuration": {
            "certificate_name": "certs1",
            "verify_depth": 1,
            "verify_peer_certificate": true
        }
       }
"""
from ansible.module_utils.basic import AnsibleModule

from ansible.module_utils.oracle import oci_utils, oci_lb_utils


try:
    from oci.load_balancer.load_balancer_client import LoadBalancerClient
    from oci.exceptions import ServiceError, ClientError
    from oci.util import to_dict
    from oci.load_balancer.models import (
        CreateBackendSetDetails,
        UpdateBackendSetDetails,
        BackendDetails,
        HealthCheckerDetails,
        SessionPersistenceConfigurationDetails,
        SSLConfigurationDetails,
    )

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False

logger = None


def create_or_update_backend_set(lb_client, module):
    backend_set = None
    result = dict(changed=False, backend_set="")
    lb_id = module.params.get("load_balancer_id")
    name = module.params.get("name")
    backend_set = oci_utils.get_existing_resource(
        lb_client.get_backend_set, module, load_balancer_id=lb_id, backend_set_name=name
    )
    try:
        if backend_set:
            result = update_backend_set(lb_client, module, lb_id, backend_set, name)
        else:
            result = oci_utils.check_and_create_resource(
                resource_type="backend_set",
                create_fn=create_backend_set,
                kwargs_create={"lb_client": lb_client, "module": module},
                list_fn=lb_client.list_backend_sets,
                kwargs_list={"load_balancer_id": lb_id},
                module=module,
                model=CreateBackendSetDetails(),
            )
    except ServiceError as ex:
        get_logger().error("Unable to create/update backend set due to: %s", ex.message)
        module.fail_json(msg=ex.message)
    except ClientError as ex:
        get_logger().error("Unable to create/update backend set due to: %s", str(ex))
        module.fail_json(msg=str(ex))

    return result


def create_backend_set(lb_client, module):
    backen_end_set_input_details = dict(
        {
            "backends": module.params.get("backends", None),
            "health_checker": module.params.get("health_checker"),
            "policy": module.params.get("policy"),
            "session_persistence_configuration": module.params.get(
                "session_persistence_configuration", None
            ),
            "ssl_configuration": module.params.get("ssl_configuration", None),
        }
    )
    name = module.params.get("name")
    lb_id = module.params.get("load_balancer_id")
    get_logger().info("Creating backend set %s in the load balancer %s", name, lb_id)
    backend_set_details = oci_lb_utils.create_backend_sets(
        dict({name: backen_end_set_input_details})
    ).get(name)
    create_backend_set_details = CreateBackendSetDetails()
    for attribute in create_backend_set_details.attribute_map:
        create_backend_set_details.__setattr__(
            attribute, getattr(backend_set_details, attribute, None)
        )
    create_backend_set_details.name = name
    result = oci_lb_utils.create_or_update_lb_resources_and_wait(
        resource_type="backend_set",
        function=lb_client.create_backend_set,
        kwargs_function={
            "create_backend_set_details": create_backend_set_details,
            "load_balancer_id": lb_id,
        },
        lb_client=lb_client,
        get_fn=lb_client.get_backend_set,
        kwargs_get={"load_balancer_id": lb_id, "backend_set_name": name},
        module=module,
    )
    get_logger().info(
        "Successfully created backend set %s in the load balancer %s", name, lb_id
    )

    return result


def update_backend_set(lb_client, module, lb_id, backend_set, name):
    result = dict(backend_set=to_dict(backend_set), changed=False)
    update_backend_set_details = UpdateBackendSetDetails()
    purge_backends = module.params.get("purge_backends")
    delete_backends = module.params.get("delete_backends")
    input_backends = oci_lb_utils.create_backends(module.params.get("backends", None))
    existing_backends = oci_utils.get_hashed_object_list(
        BackendDetails, backend_set.backends
    )
    get_logger().info("Updating backend set %s in the load balancer %s", name, lb_id)
    backends_changed = False
    if input_backends is not None:
        backends, backends_changed = oci_utils.check_and_return_component_list_difference(
            input_backends, existing_backends, purge_backends, delete_backends
        )
    if backends_changed:
        update_backend_set_details.backends = backends
    else:
        update_backend_set_details.backends = existing_backends

    input_health_checker = oci_lb_utils.create_health_checker(
        module.params.get("health_checker")
    )
    health_checker_changed = oci_utils.update_class_type_attr_difference(
        update_backend_set_details,
        backend_set,
        "health_checker",
        HealthCheckerDetails,
        input_health_checker,
    )
    policy_changed = oci_utils.check_and_update_attributes(
        update_backend_set_details,
        "policy",
        module.params.get("policy"),
        backend_set.policy,
        False,
    )
    input_session_persistence_configuration = oci_lb_utils.create_session_persistence_configuration(
        module.params.get("session_persistence_configuration", None)
    )
    session_persistence_configuration_changed = oci_utils.update_class_type_attr_difference(
        update_backend_set_details,
        backend_set,
        "session_persistence_configuration",
        SessionPersistenceConfigurationDetails,
        input_session_persistence_configuration,
    )
    input_ssl_configuration = oci_lb_utils.create_ssl_configuration(
        module.params.get("ssl_configuration", None)
    )
    ssl_configuration_changed = oci_utils.update_class_type_attr_difference(
        update_backend_set_details,
        backend_set,
        "ssl_configuration",
        SSLConfigurationDetails,
        input_ssl_configuration,
    )
    changed = (
        backends_changed
        or health_checker_changed
        or policy_changed
        or session_persistence_configuration_changed
        or ssl_configuration_changed
    )
    if changed:
        result = oci_lb_utils.create_or_update_lb_resources_and_wait(
            resource_type="backend_set",
            function=lb_client.update_backend_set,
            kwargs_function={
                "update_backend_set_details": update_backend_set_details,
                "load_balancer_id": lb_id,
                "backend_set_name": name,
            },
            lb_client=lb_client,
            get_fn=lb_client.get_backend_set,
            kwargs_get={"load_balancer_id": lb_id, "backend_set_name": name},
            module=module,
        )
        get_logger().info(
            "Successfully updated backend set %s in the load balancer %s", name, lb_id
        )
    else:
        get_logger().info(
            "No update on backend set %s in the load balancer %s as no attribute changed",
            name,
            lb_id,
        )

    return result


def delete_backend_set(lb_client, module):
    lb_id = module.params.get("load_balancer_id")
    name = module.params.get("name")
    get_logger().info("Deleting backend set %s from the load balancer %s", name, lb_id)
    result = oci_lb_utils.delete_lb_resources_and_wait(
        resource_type="backend_set",
        function=lb_client.delete_backend_set,
        kwargs_function={"backend_set_name": name, "load_balancer_id": lb_id},
        lb_client=lb_client,
        get_fn=lb_client.get_backend_set,
        kwargs_get={"load_balancer_id": lb_id, "backend_set_name": name},
        module=module,
    )
    get_logger().info(
        "Successfully deleted backend set %s from the load balancer %s", name, lb_id
    )

    return result


def set_logger(input_logger):
    global logger
    logger = input_logger


def get_logger():
    return logger


def main():
    logger = oci_utils.get_logger("oci_load_balancer_backend_set")
    set_logger(logger)
    module_args = oci_utils.get_common_arg_spec(supports_wait=True)
    module_args.update(
        dict(
            name=dict(type="str", required=True),
            load_balancer_id=dict(type="str", required=True, aliases=["id"]),
            backends=dict(type=list, required=False),
            health_checker=dict(type=dict, required=False),
            policy=dict(type="str", required=False),
            session_persistence_configuration=dict(type=dict, required=False),
            ssl_configuration=dict(type=dict, required=False),
            purge_backends=dict(type="bool", required=False, default=True),
            delete_backends=dict(type="bool", required=False, default=False),
            state=dict(
                type="str",
                required=False,
                default="present",
                choices=["present", "absent"],
            ),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        mutually_exclusive=[["purge_backends", "delete_backends"]],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    lb_client = oci_utils.create_service_client(module, LoadBalancerClient)
    state = module.params["state"]

    if state == "present":
        result = create_or_update_backend_set(lb_client, module)
    elif state == "absent":
        result = delete_backend_set(lb_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
