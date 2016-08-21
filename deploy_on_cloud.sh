#!/bin/bash

set -x
set -e

sudo apt-get install -y python python-pip

git clone https://github.com/tobegit3hub/once2016.git

cd ./once2016/

pip install -r requirements.txt

python ./website/manage.py runserver 0.0.0.0:80
