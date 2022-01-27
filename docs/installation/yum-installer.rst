Installing Using Yum
---------------------

You can use yum to install the Oracle Cloud Infrastructure Ansible Module Collection RPM.

| The RPM also installs the required dependencies: the OCI SDK for Python and Ansible.

| The following example shows how to use yum to install the Ansible Module Collection RPM:


.. Note::
    This installation uses Python version 3.6.

.. code-block:: bash

    yum -y install oraclelinux-developer-release-el7 && sudo yum install oci-ansible-collection


To test the installation of the RPM and configuration of the SDK, you can run a sample playbook. For example:

.. code-block:: bash

    ansible-playbook-3 /usr/share/doc/oci-ansible-collection-<version>/samples/object_storage/get_namespace/sample.yaml
