#!/bin/bash
apt-get update
apt-get install -y python3-dev
pip install -r requirements.txt
MYSQLCLIENT_CFLAGS=-I/path/to/mysqlclient
MYSQLCLIENT_LDFLAGS=-L/path/to/mysqlclient