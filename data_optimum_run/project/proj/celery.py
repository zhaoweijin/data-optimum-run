#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import absolute_import
from celery import Celery,platforms

app = Celery('proj', include=['proj.tasks'])
platforms.C_FORCE_ROOT = True
app.config_from_object('proj.config')

if __name__ == '__main__':
    app.start()