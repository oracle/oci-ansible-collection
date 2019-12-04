# Install the various versions of python and related tools, in a gitlab runner
# machine. All CI jobs of the OCI ansible cloud modules project assumes the
# python installations below, and so this is a pre-requisite for running CI jobs.

# Instructions to configure the gitlab runner after installing these
# pre-reqs is at the end of this file

WKSP_ROOT="/scratch/sithyaga"
INSTALLDIR="$WKSP_ROOT/python-installs"
VENVDIR="$WKSP_ROOT/python-venvs"

mkdir -p $INSTALLDIR
mkdir -p $VENVDIR

# Pre-requisites for CI jobs
# source: https://danieleriksson.net/2017/02/08/how-to-install-latest-python-on-centos/
# Start by making sure your system is up-to-date
yum update
# Compilers and related tools
yum groupinstall -y "development tools"
# Libraries needed during compilation to enable all features of Python
yum install -y zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel expat-devel
# If you are on a clean "minimal" install of CentOS you also need the wget tool
yum install -y wget

# Install Python
# Python 2.7.14
cd $INSTALLDIR
wget http://python.org/ftp/python/2.7.14/Python-2.7.14.tar.xz
tar xf Python-2.7.14.tar.xz
cd Python-2.7.14
./configure --prefix=$INSTALLDIR --enable-unicode=ucs4 --enable-shared
make && make altinstall

# Python 3.6.4
cd $INSTALLDIR
wget http://python.org/ftp/python/3.6.4/Python-3.6.4.tar.xz
tar xf Python-3.6.4.tar.xz
cd Python-3.6.4
./configure --prefix=$INSTALLDIR --enable-shared LDFLAGS="-Wl,-rpath /usr/local/lib"
make && make altinstall

# Python 3.5.5
cd $INSTALLDIR
wget http://python.org/ftp/python/3.5.5/Python-3.5.5.tar.xz
tar xf Python-3.5.5.tar.xz
cd Python-3.5.5
./configure --prefix=$INSTALLDIR --enable-shared LDFLAGS="-Wl,-rpath /usr/local/lib"
make && make altinstall


# Install pip, setuptools, wheel
cd $INSTALLDIR
export PATH="$INSTALLDIR/bin:$PATH"
export LD_LIBRARY_PATH="$INSTALLDIR/lib:$LD_LIBRARY_PATH"

# First get the script:
wget https://bootstrap.pypa.io/get-pip.py

# Then execute it using Python 2.7 and/or Python 3.6
python2.7 get-pip.py
# for 2.7 this needs to be run in addition to get-pip.py
python2.7 -m ensurepip --default-pip

python3.5 get-pip.py
python3.6 get-pip.py


# After running this script follow the instructions at
# https://gitlab-odx.oracledx.com/odx/gitlab-ee-setup/blob/master/runner/README.md
# and https://docs.gitlab.com/runner/ to install and register the
# gitlab-runner in the machine.

# - install the gitlab-runner using the instructions in https://docs.gitlab.com/runner/install/linux-repository.html

# -Setup certs for runner using instructions in https://gitlab-odx.oracledx.com/odx/gitlab-ee-setup/blob/master/runner/README.md#setup-the-certs-and-proxies-for-the-runner
# Convert pem format certs to crt format before copying over using
# $ openssl x509 -outform der -in Combined-VTN-Oracle-SHA2.pem -out gitlab-odx.oracle.com.crt

# - In systemd configuration for gitlab-runner-service.d setup proxy
# settings. Use instructions in
# https://gitlab-odx.oracledx.com/odx/gitlab-ee-setup/blob/master/runner/README.md#setup-the-certs-and-proxies-for-the-runner
# to perform this step

# - register the runner using the gitlab-ci token in the gitlab
# project's CI/CD settings page
# (https://gitlab-odx.oracledx.com/oci/ansible-cloud-module/settings/ci_cd)

# - Install the gitlab-runner as a systemd service by running:
#   - # gitlab-runner install

# - configure the runner in `/etc/gitlab-runner/config.toml`. Add an entry
# for pre_clone_script, environment and one for builds_dir to point to a local
# directory. Ensure that a directory is created for the value pointed to
# by `builds_dir`.
# A sample is shown below:
# ----- sample /etc/gitlab-runner/config.toml --------
# concurrent = 1
# check_interval = 0
#
# [[runners]]
#   name = "slc16fdw"
#   url = "https://gitlab-odx.oracledx.com/"
#   token = "18e42c39157990a9ddd72f3d51ee55"
#   executor = "shell"
#   pre_clone_script = "git config --global http.proxy $HTTP_PROXY; git config --global https.proxy $HTTPS_PROXY"
#   environment = ["HTTPS_PROXY=http://www-proxy.us.oracle.com:80", "HTTP_PROXY=http:www-proxy.us.oracle.com:80","no_proxy=.oracle.com,.grungy.us,docker"]
#   builds_dir="/scratch/sithyaga/builds-dir"
#   [runners.cache]
# ----- sample /etc/gitlab-runner/config.toml --------


# Also install Mcafee in the gitlab runner for malware analysis
# There appears to be no way to install mcafee in silent mode. So for now, assuming mcafee is installed
# manually in all gitlab runners.
# Install Mcafee using the following instructions
# src: https://confluence.oraclecorp.com/confluence/display/GPS/Malware+Scanning
unset ftp_proxy
cd $WKSP_ROOT

export MCAFEE_ROOT="$WKSP_ROOT/mcafee"
mkdir -p $MCAFEE_ROOT
cd $MCAFEE_ROOT
VS_FILE="vscl-l64-606-l.tar.gz"
wget --verbose -P $MCAFEE_ROOT "ftp://obiftp.us.oracle.com/modules/unlicensed/global/mcafee/clscanners/linux_64/$VS_FILE"
tar -zxvf "$MCAFEE_ROOT/$VS_FILE"
./install-uvscan "$MCAFEE_ROOT"
