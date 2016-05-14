#!/usr/bin/env bash

# Update Repositories

# Add Ansible Repository & Install Ansible
sudo add-apt-repository -y ppa:ansible/ansible
sudo apt-get update
sudo apt-get install -y software-properties-common ansible git

#Galaxy roles installation
sudo ansible-galaxy install -r ./install_roles.yml

sudo ansible-playbook ./playbook.yml -e hostname=stepic.lan --connection=local -v