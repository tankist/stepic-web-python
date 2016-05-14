#!/usr/bin/env bash

# Update Repositories

# Add Ansible Repository & Install Ansible
#sudo add-apt-repository -y ppa:ansible/ansible
sudo apt-get update
sudo apt-get install -y software-properties-common ansible git

sudo ansible-playbook ./server_playbook.yml -e hostname=stepic.lan --connection=local -v