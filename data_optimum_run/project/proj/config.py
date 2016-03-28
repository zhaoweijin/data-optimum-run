#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import absolute_import

CELERY_RESULT_BACKEND = 'amqp'
BROKER_URL = 'amqp://localhost'

CELERY_TIMEZONE = 'Asia/Shanghai'

# from datetime import timedelta
#
# CELERYBEAT_SCHEDULE = {
#     'add-every-30-seconds': {
#          'task': 'proj.tasks.add',
#          'schedule': timedelta(seconds=30),
#          'args': (16, 16)
#     },
# }


from celery.schedules import crontab

CELERYBEAT_SCHEDULE = {
    # Executes every Monday morning at 7:30 A.M
    'add-every-15-minutes': {
        'task': 'proj.tasks.add',
        'schedule': crontab(minute='*/15'),
        'args': (16, 16),
    },
    'add-every-10-minutes': {
        'task': 'proj.tasks.add2',
        'schedule': crontab(minute='*/10'),
        'args': (10, 10),
    },
    # 'add-every-10-minutes': {
    #     'task': 'proj.tasks.arch',
    #     'schedule': crontab(minute='*/1'),
    #     'args': (10, 10),
    # },
}