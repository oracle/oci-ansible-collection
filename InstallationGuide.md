## Installation Steps:
```
    sudo pip3 install virtualenv
    virtualenv venvansible
    source venvansible/bin/activate
    pip3 install oci
    pip3 install ansible
    ansible-galaxy collection install -f oracle.oci
```

To test the installation, you can run this sample:
```
venvansible/bin/ansible-playbook -vvv ~/.ansible/collections/ansible_collections/oracle/oci/samples/object_storage/get_namespace/sample.yaml
```

## How to troubleshoot installation errors?
#### Troubleshoot the error `oci python sdk required for this module`

You will get an error if Ansible runs using python2 and the python SDK is installed under python 3.<br/>
The above installation should run python from the virtual env path: `venvansible/bin/python`.<br/>
You should see this in the logs when running the playbook using -vvv flag:
`venvansible/bin/python /Users/.ansible/tmp/ansible-tmp/AnsiballZ_setup.py`<br/>
Make sure Ansible is not using `/usr/bin/python` when running:
`/usr/bin/python /Users/.ansible/tmp/ansible-tmp/AnsiballZ_setup.py`<br/>
Refer to Ansible python 3 support: https://docs.ansible.com/ansible/2.4/python_3_support.html

Note: Ansible only uses the current python environment if you are using the implicit localhost i.e if you use the 
host as localhost and do not define any host configuration. Else it goes through the interpreter discovery process 
'and picks the first one. It provides a configuration setting (both at system level and the host level) to 
explicitly set the python interpreter to use. <br/>
Please check https://docs.ansible.com/ansible/latest/reference_appendices/interpreter_discovery.html. Please set it 
to the environment (path to python executable) where OCI python SDK is installed and re-run the playbook.
 