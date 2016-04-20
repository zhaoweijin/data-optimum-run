#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import json
import time
import sys

import datetime

import os
import re
import copy
import pycurl
from StringIO import StringIO
from random import randrange
from random import randint
# Insert project root path to sys.path
from sqlalchemy import func

project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../'))
if project_path not in sys.path:
    sys.path.insert(0, project_path)

from application import create_app
from application.models import db
from application.models import WpPosts
from application.models import WpTermRelationships
from application.models import WpDataoptimumRecord
from application.models import WpDataoptimumPlayContentAuto

reload(sys)
sys.setdefaultencoding('utf-8')

class Backend(object):

    def __init__(self):
        app = create_app()
        self.app = app

    def getContent(self,url):


        buffer = StringIO()
        c = pycurl.Curl()
        c.setopt(c.URL, url)
        c.setopt(c.WRITEDATA, buffer)
        c.setopt(c.CONNECTTIMEOUT, 10)
        c.setopt(c.TIMEOUT, 10)

        try:
            c.perform()
        except pycurl.error, e:
            raise e
        # c.perform()
        c.close()

        body = buffer.getvalue()
        # Body is a string in some encoding.
        # In Python 2, we can print it without knowing what the encoding is.
        return body

    def random_date(self,start,l):
        current = start
        while l >= 0:
            current = current + datetime.timedelta(minutes=randrange(60))
            yield current
            l-=1

    def excute(self,page):
        times = datetime.datetime.now().strftime("%Y-%m-%d")
        # content = self.getContent('http://www.appgame.com/?json=get_date_posts&date=2016-04-14&count=2')
        if page==1:
            content = self.getContent('http://www.appgame.com/?json=get_date_posts&date='+times)
        else:
            content = self.getContent('http://www.appgame.com/?json=get_date_posts&date='+times+'&page='+str(page))

        content = json.loads(content)
        page_num = content['pages']


        for i in content['posts']:
            with self.app.app_context():
                val = WpDataoptimumPlayContentAuto.query.filter(WpDataoptimumPlayContentAuto.url==i['url']).first()
                if val is None:
                    num = randint(2, 5)
                    #select user
                    list_user = WpPosts.query.outerjoin(WpTermRelationships,WpPosts.ID==WpTermRelationships.object_id).filter((
        WpTermRelationships.term_taxonomy_id.in_([152,159,161]))).with_entities(WpPosts.ID,'post_title','post_type',WpTermRelationships.term_taxonomy_id).order_by(func.rand()).limit(num).all()
                    #select content
                    list_content = WpDataoptimumRecord.query.filter((WpDataoptimumRecord.category.like('%152%'))|(WpDataoptimumRecord.category.like('%159%'))|(WpDataoptimumRecord.category.like('%161%'))).order_by(func.rand()).limit(num).all()
                    lists = {}
                    if len(list_user) == len(list_content):
                        for index in range(num):
                            lists[index]={"username":list_user[index].post_title,"content":list_content[index].comments}

                    #set time
                    list_time = []
                    startDate = datetime.datetime.now()
                    for x in list(self.random_date(startDate,num)):
                        list_time.append(x.strftime("%Y-%m-%d %H:%M:%S"))

                    for index2 in lists:
                        me = WpDataoptimumPlayContentAuto(lists[index2]['username'],lists[index2]['content'],i['url'],list_time[index2])
                        db.session.add(me)
                        db.session.commit()

        if page<page_num:
            page += 1
            self.excute(page)

    def run(self):
        self.excute(1)