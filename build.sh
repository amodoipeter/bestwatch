#!/bin/bash
apt-get update
apt-get upgrade
apt-get install -y python3
apt-get install -y python3-pip
apt-get install -y python3-dev
pip install -r requirements.txt
MYSQLCLIENT_CFLAGS=-I/path/to/mysqlclient
MYSQLCLIENT_LDFLAGS=-L/path/to/mysqlclient