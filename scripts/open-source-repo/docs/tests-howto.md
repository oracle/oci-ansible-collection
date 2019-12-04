# How to run OCI Ansible Module Tests

## Unit Tests

In a virtual environment, install all pre-requisites listed in the
[OCI Ansible Modules Getting Started](https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/ansiblegetstarted.htm) documentation page.

To run unit tests as a developer, follow these steps:

```sh
$ # install all unit test dependencies
$ pip install pytest nose mock pytest-mock
$ python -m pytest -r a --fulltrace --color yes test/units/
```

