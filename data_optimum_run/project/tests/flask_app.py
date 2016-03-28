#!/usr/bin/env python
#coding=utf-8


import sys
import os

# Insert project root path to sys.path
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_path not in sys.path:
    sys.path.insert(0, project_path)


from application import create_app
from application.models import WpDataoptimumRecord
from application.models import WpDataoptimumPlay
from application.models import WpDataoptimumPlayContent

# app = create_app()

class BaseSuite(object):
    def setup(self):
        # os.environ['MODE'] = 'TESTING'

        app = create_app()
        # self.app = app
        # self.client = app.test_client()
        with app.app_context():
            # me = WpDataoptimumRecord.query.filter((WpDataoptimumRecord.state==1)).first()
            val = WpDataoptimumPlayContent.query.join(WpDataoptimumPlay,WpDataoptimumPlayContent.play_id==WpDataoptimumPlay.id).filter(WpDataoptimumPlayContent.status==0)
            print val.title,val.post_url
            # db.drop_all()
            # db.create_all()

    # def teardown(self):
    #     with self.app.app_context():
    #         db.drop_all()


test = BaseSuite()
test.setup()