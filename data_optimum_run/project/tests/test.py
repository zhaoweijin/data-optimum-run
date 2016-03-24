#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import os

# Insert project root path to sys.path
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_path not in sys.path:
    sys.path.insert(0, project_path)

# import time
# import MySQLdb

from config import load_config
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


app = Flask(__name__)
# Load config
config = load_config()
app.config.from_object(config)

db.init_app(app)




# ltime=time.localtime(1395025933)
# timeStr=time.strftime("%Y-%m-%d %H:%M:%S", ltime)


# a = "2013-10-10 23:40:00"
# time_stamp = time.mktime(time.strptime(a,'%Y-%m-%d %H:%M:%S'))
#
#
#
#
# print int(timeStamp)
# print timeStr
# print int(time.time())
# print time.time()
# print time.localtime()

print config