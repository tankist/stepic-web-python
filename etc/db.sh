#!/usr/bin/env bash

mysql -u root -e "create user 'ask'@'localhost' identified by 'ask'"
mysql -u root -e "create database ask default character set=utf8"
mysql -u root -e "grant all privileges on ask. * to 'ask'@'localhost'"

python manage.py syncdb

mysql -u ask -p ask -e "alter table qa_question modify column added_at date default null"
