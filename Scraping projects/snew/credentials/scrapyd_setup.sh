#!/bin/sh
# This is a comment!
echo "=============== installing sprayd and scrapy ==============="
pip3 install scrapy
pip3 install scrapyd
pip3 install git+https://github.com/scrapy/scrapyd-client

 echo "=============== creating folders ==============="
 sudo mkdir -p /etc/scrapyd/ && sudo touch /etc/scrapyd/scrapyd.conf
 sudo mkdir -p ~/usr/scrapyd/eggs && sudo mkdir -p ~/usr/scrapyd/logs
 sudo mkdir -p ~/usr/scrapyd/items && sudo mkdir -p ~/usr/scrapyd/dbs

# asd
# chmod +x scrapyd_setup.sh
# put in scrapy project

# #!/usr/bin/env python
#
# from setuptools import setup, find_packages
#
# setup(
#     name =          'snew_thingy',
#     version =       '1.1',
#     packages =      find_packages(),
#     entry_points =  {'scrapy': ['settings = snew.settings']},
# )

# RUN TO EGGIFY
# python3 setup.py bdist_egg
# curl http://localhost:6800/addversion.json -F project=news -F version=0.1 -F egg=/home/snew/dist/news-0.1-py3.5.egg


# UPLOAD THE PROJECT
# curl http://localhost:6800/addversion.json -F project=snew_thingy -F version=1.0 -F egg=@dist/snew_thingy-1.0-py3.6.egg
# curl http://localhost:6800/addversion.json -F project=snew -F version=1.4 -F egg=@dist/snew-1.4-py3.6.egg
# curl http://0.0.0.0:6869/addversion.json -F project=snew -F version=1.6 -F egg=@dist/snew-1.6-py3.6.egg
curl http://0.0.0.0:6869/addversion.json -F project=news -F version=1.8 -F egg=@dist/news-1.8-py2.7.egg
curl http://0.0.0.0:6869/addversion.json -F project=news -F version=1.9 -F egg=@dist/news-1.9-py3.6.egg
curl http://0.0.0.0:6869/addversion.json -F project=news -F version=2.0 -F egg=@dist/news-2.0-py3.6.egg
curl http://0.0.0.0:6869/addversion.json -F project=news -F version=2.0 -F egg=@dist/news-2.0-py2.7.egg
curl http://0.0.0.0:6800/addversion.json -F project=news -F version=0.1 -F egg=@dist/news-0.1-py3.5.egg

curl http://localhost:6800/listspiders.json?project=news
curl http://localhost:6800/addversion.json -F project=news -F version=1.8 -F egg=@dist/snew-1.8-py3.6.egg
curl http://localhost:6800/listspiders.json?project=news
curl http://0.0.0.0:6869/listspiders.json?project=news
curl http://0.0.0.0:6800/listspiders.json?project=news
# update PATH python to include credentials


# echo "export PYTHONPATH=/Users/ilyaperepelitsa/quant/credentials:\$PYTHONPATH" >> ~/.bash_profile
# source ~/.bash_profile


# ssh -i "yamacake.pem" ec2-user@ec2-18-218-162-35.us-east-2.compute.amazonaws.com
# sudo find . -print | grep -i 'scrapyd'
# sudo vim /etc/scrapyd/scrapyd.conf
# curl http://localhost:6800/schedule.json -d project=news -d spider=techcrunch
# curl http://0.0.0.0:6800/schedule.json -d project=news -d spider=techcrunch
# curl http://24.188.105.21:6800/schedule.json -d project=news -d spider=techcrunch




# dist/news-0.1-py3.5.egg
