#!/bin/bash

#rm -rf dist/*
#rm -rf build/
#pycodestyle --exclude='*testfiles*' . | grep -v 'build' | grep -v 'dist' | grep -v 'W605'> logs/pep8.log
#python3 setup.py sdist bdist_wheel  > logs/install-pip.log
#pip3 uninstall kotaix  -y  >> logs/install-pip.log
#ls -R /Users/oscarab/Library/Python/3.9/lib/python/site-packages/kotaix/
#pip3 install dist/kotaix-*.whl >> logs/install-pip.log
#tar tvf dist/kotaix-0.1.tar.gz
#ls -l /usr/local/lib/python3.10/site-packages/kotaix/
#ls -R /Users/oscarab/Library/Python/3.9/lib/python/site-packages/kotaix/ #>> logs/install-pip.log
#python3 -m kotaix testfiles/
#kotaix testfiles/
#cat kotaix_report.txt

python3 -m venv env
source env/bin/activate
pip install scikit-learn
