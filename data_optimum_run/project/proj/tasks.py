#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import absolute_import
from proj.celery import app
from application.com.appgame.jp import archives
from application.com.appgame.www import backend

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
    return 1

@app.task
def getUrl():
    s = backend.Backend()
    s.run()
    return 2