# Copyright (c) 2018, 2019, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from ansible.module_utils.oracle import oci_utils

try:
    from oci.util import to_dict
    from oci.exceptions import ServiceError

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


logger = oci_utils.get_logger("oci_compute_utils")


def _debug(s):
    get_logger().debug(s)


def get_logger():
    return logger


def get_volume_attachments(compute_client, instance):
    param_map = {
        "instance_id": instance["id"],
        "compartment_id": instance["compartment_id"],
    }

    volume_attachments = to_dict(
        oci_utils.list_all_resources(
            compute_client.list_volume_attachments, **param_map
        )
    )
    return volume_attachments


def get_boot_volume_attachment(compute_client, instance):
    param_map = {
        "availability_domain": instance["availability_domain"],
        "instance_id": instance["id"],
        "compartment_id": instance["compartment_id"],
    }

    boot_volume_attachments = to_dict(
        oci_utils.list_all_resources(
            compute_client.list_boot_volume_attachments, **param_map
        )
    )

    if boot_volume_attachments:
        return boot_volume_attachments[0]
    return None


def get_primary_ips(compute_client, network_client, instance):
    primary_public_ip = None
    primary_private_ip = None

    vnic_attachments = oci_utils.list_all_resources(
        compute_client.list_vnic_attachments,
        compartment_id=instance["compartment_id"],
        instance_id=instance["id"],
    )

    if vnic_attachments:
        for vnic_attachment in vnic_attachments:
            if vnic_attachment.lifecycle_state == "ATTACHED":
                try:
                    vnic = network_client.get_vnic(vnic_attachment.vnic_id).data
                    if vnic.is_primary:
                        if vnic.public_ip:
                            primary_public_ip = vnic.public_ip
                        if vnic.private_ip:
                            primary_private_ip = vnic.private_ip
                except ServiceError as ex:
                    if ex.status == 404:
                        get_logger().debug(
                            "Either VNIC with ID %s does not exist or you are not authorized to access it.",
                            vnic_attachment.vnic_id,
                        )

    return primary_public_ip, primary_private_ip


def get_iscsi_attach_commands(volume_attachment):
    if not volume_attachment.get("attachment_type") == "iscsi":
        return []
    iqn = volume_attachment.get("iqn")
    ipv4 = volume_attachment.get("ipv4")
    port = volume_attachment.get("port")
    chap_username = volume_attachment.get("chap_username")
    chap_secret = volume_attachment.get("chap_secret")
    iscsi_attach_commands = [
        "sudo iscsiadm -m node -o new -T {0} -p {1}:{2}".format(iqn, ipv4, port),
        "sudo iscsiadm -m node -o update -T {0} -n node.startup -v automatic".format(
            iqn
        ),
    ]
    if chap_username:
        iscsi_attach_commands.extend(
            [
                "sudo iscsiadm -m node -T {0} -p {1}:{2} -o update -n node.session.auth.authmethod -v CHAP".format(
                    iqn, ipv4, port
                ),
                "sudo iscsiadm -m node -T {0} -p {1}:{2} -o update -n node.session.auth.username -v {3}".format(
                    iqn, ipv4, port, chap_username
                ),
                "sudo iscsiadm -m node -T {0} -p {1}:{2} -o update -n node.session.auth.password -v {3}".format(
                    iqn, ipv4, port, chap_secret
                ),
            ]
        )
    iscsi_attach_commands.append(
        "sudo iscsiadm -m node -T {0} -p {1}:{2} -l".format(iqn, ipv4, port)
    )
    return iscsi_attach_commands


def get_iscsi_detach_commands(volume_attachment):
    if not volume_attachment.get("attachment_type") == "iscsi":
        return []
    return [
        "sudo iscsiadm -m node -T {0} -p {1}:{2} -u".format(
            volume_attachment.get("iqn"),
            volume_attachment.get("ipv4"),
            volume_attachment.get("port"),
        ),
        "sudo iscsiadm -m node -o delete -T {0}".format(volume_attachment.get("iqn")),
    ]


def with_iscsi_commands(volume_attachment):
    volume_attachment["iscsi_attach_commands"] = get_iscsi_attach_commands(
        volume_attachment
    )
    volume_attachment["iscsi_detach_commands"] = get_iscsi_detach_commands(
        volume_attachment
    )
    return volume_attachment
