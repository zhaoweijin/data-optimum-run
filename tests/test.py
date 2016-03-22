#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
# ltime=time.localtime(1395025933)
# timeStr=time.strftime("%Y-%m-%d %H:%M:%S", ltime)


a = "2013-10-10 23:40:00"
time_stamp = time.mktime(time.strptime(a,'%Y-%m-%d %H:%M:%S'))




print int(timeStamp)
print timeStr
print int(time.time())
print time.time()
print time.localtime()