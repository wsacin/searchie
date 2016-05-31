# Searchie

| Main Technologies        |
|--------------------------|
| Python 3                 |
| Django 1.9.6             |
| Bootstrap 3              |
| Elasticsearch (Haystack) |
| PostgreSQL               |
| Ansible                  |

## Getting Started

### Clone the repo and install virtualenv

```bash
git clone https://github.com/wsacin/searchie.git
```

> If you are familiar with the Ansible automation tool, you can proceed
> to the playbooks section.

Begin installing python 3 and virtualenv. For debian based architectures:

```bash
$ sudo apt-get install python3-pip
$ sudo pip3 install virtualenv
```

Now you can create and enter a virtualenv to install the project's requirements on:

```bash
$ virtualenv /path/to/env
$ source /path/to/env/bin/activate
```

Install searchie's python requirements:

```bash
$ pip3 install /path/to/searchie/requirements.txt # no sudo
```

### System dependencies

Some dependencies have to be installed on the system. Check out on Searchie's playbook role "common" on:
> searchie_playbooks/roles/common/tasks/main.yaml

there you will find every system package that Searchie uses. To install Searchie's dependencies via playbooks, first install Ansible:

```bash
$ pip3 install ansible
```
Now you can run Seachie's playbooks. But first make them work with your configurations. Put your hosts in searchie_playbooks/webservers.yml. For example:
```yaml
[webservers]
searchie_server ansible_ssh_host=<your_hosts_ip> ansible_ssh_port=22
```
Now you can run playbooks for installing and configuring Searchie:
```bash
ansible-playbook -i webservers.yml searchie.yml -u <your_remote_user> --become-user=root -K -k
```
You can run role by role with `--tags` or `-t`, for example:
```bash
ansible-playbook -i webservers.yml searchie.yml -u <your_remote_user> --become-user=root -K -k -t "common,searchie"
```
The above command will run the instalation of system and env packages, and
clone Searchie's latest version from github to the directory configured in
"searchie-playbooks/group_vars/all". There you can customize the names and
directories to be deployed.

### Running
Once everything was installed and every playbook ran, all the services needed for searchie should be up and running. You can stop and start every service with the
services role, by the tags `stopServices` and `startServices`.