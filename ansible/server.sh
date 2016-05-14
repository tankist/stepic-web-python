#!/usr/bin/env bash

# Update Repositories

# Add Ansible Repository & Install Ansible
#sudo add-apt-repository -y ppa:ansible/ansible
sudo apt-get update
sudo apt-get install -y software-properties-common ansible git

# Setup Ansible for Local Use and Run
sudo cp ./inventories/dev /etc/ansible/hosts -f
sudo chmod 666 /etc/ansible/hosts
cat ./files/authorized_keys >> /home/box/.ssh/authorized_keys

sudo ansible-playbook ./server_playbook.yml -e hostname=stepic.lan --connection=local -v