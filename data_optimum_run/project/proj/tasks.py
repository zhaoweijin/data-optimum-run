#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import absolute_import
from proj.celery import app
from application.com.appgame.jp import archives
# from application.com.appgame.jp import archives_c

# @app.task
# def add(x, y):
#     return x + y
#
# @app.task
# def add2(x, y):
#     return x + y

@app.task
def arch(x, y):
    # archives.firefoxLink1(1,2,3)
    s = archives.firefoxLink()
    s.run()
    return 1234

# @app.task
# def arch2(x, y):
#     s = archives_c.firefoxLink("http://jp.appgame.com/archives/257239.html")
#     s.run()
#     return 11