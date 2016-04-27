#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import json
import time
import sys

import datetime

import os

import pycurl
from StringIO import StringIO

project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../'))
if project_path not in sys.path:
    sys.path.insert(0, project_path)

from application import create_app
from application.models import db
from application.models import WpDataoptimumUrls
from application.models import WpDataoptimumPlay
from application.models import WpDataoptimumUrls

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
                urls = WpDataoptimumUrls.query.filter(WpDataoptimumUrls.url==i['url']).first()
                if urls is None:
                    val = WpDataoptimumPlay.query.filter(WpDataoptimumPlay.post_url==i['url']).first()
                    if val is None:
                        #set time

                        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        me = WpDataoptimumPlay(i['url'],i['title'],'',time,time)
                        db.session.add(me)
                        db.session.commit()

        if page<page_num:
            page += 1
            self.excute(page)

    def run(self):
        self.excute(1)
