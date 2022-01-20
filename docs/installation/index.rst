





Installation
~~~~~~~~~~~~

This topic describes how to install Oracle Cloud Infrastructure Ansible Collection


==============
Prerequisites
==============

* python >= 3.6


===================
Installation steps
===================

You can use the following ways to install(or upgrade) OCI Ansible Collection


Oracle Linux 7
---------------

.. code-block:: bash

    sudo yum-config-manager --enable ol7_developer
    sudo yum-config-manager --enable ol7_developer_EPEL
    sudo yum install oci-ansible-collection

    # to upgrade oci-ansible-collection
    sudo yum update oci-ansible-collection


Oracle Linux 8
---------------

.. code-block:: bash

    sudo yum-config-manager --enable ol8_developer
    sudo yum-config-manager --enable ol8_developer_EPEL
    sudo yum install oci-ansible-collection

    # to upgrade oci-ansible-collection
    sudo yum update oci-ansible-collection


Linux/macOS
---------------
.. warning::
    On some Linux distributions, ``python-venv`` support is not there. The script installs the necessary dependencies which require ``sudo`` access. Ensure that the current user has sudo permissions before beginning to install the script.
     

.. code-block:: bash

    curl -L https://raw.githubusercontent.com/oracle/oci-ansible-collection/master/scripts/install.sh | bash -s -- --verbose

    # to upgrade oci-ansible-collection
    curl -L https://raw.githubusercontent.com/oracle/oci-ansible-collection/master/scripts/install.sh | bash -s -- --verbose --upgrade


Manual
-------

.. code-block:: bash

    sudo pip3 install virtualenv
    virtualenv venvansible
    source venv ansible/bin/activate
    pip3 install oci
    pip3 install ansible
    ansible-galaxy collection install -f oracle.oci


===================
Installation guide
===================

You may check the following document(s) for more details:

.. toctree::
    :maxdepth: 1

    Installation Guide <installation-guide.rst>

