Installation
~~~~~~~~~~~~

This topic describes how to install ( or upgrade) Oracle Cloud Infrastructure Ansible Collection


Prerequisites
---------------

* python >= 3.6


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

Please check :doc:`Installation Using Yum<yum-installer>` for more details.

Linux/macOS
---------------
.. warning::
    On some Linux distributions, ``python-venv`` support is not there. The script installs the necessary dependencies which require ``sudo`` access. Ensure that the current user has sudo permissions before beginning to install the script.
     

.. code-block:: bash

    curl -L https://raw.githubusercontent.com/oracle/oci-ansible-collection/master/scripts/install.sh | bash -s -- --verbose

    # to upgrade oci-ansible-collection
    curl -L https://raw.githubusercontent.com/oracle/oci-ansible-collection/master/scripts/install.sh | bash -s -- --verbose --upgrade

Please check :doc:`Installation Script<installer-script>` for more details.

Manual
-------

.. code-block:: bash

    sudo pip3 install virtualenv
    virtualenv venvansible
    source venv ansible/bin/activate
    pip3 install oci
    pip3 install ansible
    ansible-galaxy collection install -f oracle.oci
