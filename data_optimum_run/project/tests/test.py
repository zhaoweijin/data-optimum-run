#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
import MySQLdb
# from config.development import DevelopmentConfig
from config import load_config

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

print DevelopmentConfig.DATABASE_HOST