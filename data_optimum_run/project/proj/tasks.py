#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import absolute_import
from proj.celery import app
from application.com.appgame.jp import archives

@app.task
def add(x, y):
    return x + y

@app.task
def add2(x, y):
    return x + y

@app.task
def arch(x, y):
    # archives.firefoxLink1(1,2,3)
    s = archives.firefoxLink("http://jp.appgame.com/archives/251011.html")
    s.run()
    return 1234