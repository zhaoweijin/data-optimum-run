#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import sys
import copy
import os
import re
import datetime

# Insert project root path to sys.path
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../'))
if project_path not in sys.path:
    sys.path.insert(0, project_path)

from selenium import webdriver
from selenium.common.exceptions import TimeoutException,NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from application import create_app
from application.models import db
from application.models import WpDataoptimumPlay
from application.models import WpDataoptimumPlayContent
import traceback

reload(sys)
sys.setdefaultencoding('utf-8')


class firefoxLink(object):
    """Summary of class here.

    function go1 webdriver step1
    function go2 webdriver step2
    function go3 webdriver step3


    Attributes:
        data_c: dict of data that contains the parent layer.
        driver: object of webdriver.
        url: string of url.
    """
    def __init__(self,url):
        """Inits webdriver and data."""
        self.url = url

        app = create_app()
        self.app = app
        with app.app_context():
            list = WpDataoptimumPlayContent.query.outerjoin(WpDataoptimumPlay,WpDataoptimumPlayContent.play_id==WpDataoptimumPlay.id).filter(WpDataoptimumPlayContent.carry_time>="2016-03-28 14:15:01").with_entities(WpDataoptimumPlayContent.id,'title','username','from_user','to_user','self_symbol','object_symbol','content','play_id','carry_time',WpDataoptimumPlayContent.status).all()

        data = {}
        parent = {}
        for val in list:
            d = {"id":val.id,"title":val.title,"username":val.username,"from_user":val.from_user,"to_user":val.to_user,"self_symbol":val.self_symbol,"object_symbol":val.object_symbol,"content":val.content,"play_id":val.play_id,"carry_time":val.carry_time,"status":val.status}
            data[val.id] = d

        for val in data:
            pid = data[val]['self_symbol'] + str(data[val]['play_id'])
            data[val]['pid'] = pid
            parent[pid] = data[val]

        pid = ''
        self.data_c = copy.deepcopy(data)
        # get parent data
        for val in list:
            if val.object_symbol:
                pid = val.object_symbol + str(val.play_id)
                if pid in parent.keys():
                    self.data_c[val.id]['parent'] = parent[pid]

    def __call__(self,func,*args):
        try:
            func(*args)
        except TimeoutException:
            self.log_error()
            self.driver.execute_script('window.stop()')
        except NoSuchElementException:
            self.log_error()
            self.driver.quit()
            self.driver.session_id = None
        except:
            self.log_error()
            self.driver.quit()
            exit()
        #     print "Unexpected error:", sys.exc_info()[0]
        #     self.driver.quit()
        #     raise


    def log_error(self):
        f=open(project_path+"/log/app/jp.appgame.com-"+datetime.datetime.now().strftime("%Y%m%d")+".txt",'a')
        traceback.print_exc(file=f)
        f.flush()
        f.close()


    def go1(self):
        self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',desired_capabilities=DesiredCapabilities.FIREFOX)
        self.driver.set_page_load_timeout(30)
        self.driver.get(self.url)
        time.sleep(3)
        self.driver.switch_to.frame(self.driver.find_element_by_id("commentics-iframe"))
        #To continue with the default content do
        # driver.switch_to.default_content()
        self.driver.find_element_by_css_selector("a.sso_login").click()


    def go2(self,username):
        if self.driver.session_id is not None:
            time.sleep(3)
            self.driver.find_element_by_id("email").clear()
            self.driver.find_element_by_id("email").send_keys(username)
            self.driver.find_element_by_id("password").clear()
            self.driver.find_element_by_id("password").send_keys(111111)
            self.driver.find_element_by_link_text(u"登录").click()
            time.sleep(5)
            self.driver.switch_to.frame(self.driver.find_element_by_id("commentics-iframe"))



    def go3(self,content,id,point=''):
        if self.driver.session_id is not None:
            if not point:
                self.driver.find_element_by_name("cmtx_comment").clear()
                self.driver.find_element_by_name("cmtx_comment").send_keys(content)
                self.driver.find_element_by_link_text(u"评论").click()
            else:
                point.find_element_by_css_selector("a.cmtx_reply_enabled").click()
                point.find_element_by_name("cmtx_comment").clear()
                point.find_element_by_name("cmtx_comment").send_keys(content)
                point.find_element_by_link_text(u"评论").click()
            time.sleep(3)
            with self.app.app_context():
                WpDataoptimumPlayContent.query.filter(WpDataoptimumPlayContent.id==id).update({WpDataoptimumPlayContent.status : 1})
                db.session.commit()

    def run(self):
        for val in self.data_c:
            id = self.data_c[val]['id']
            username = self.data_c[val]['username']
            from_user = str(self.data_c[val]['from_user'])
            to_user = str(self.data_c[val]['to_user'])
            content = self.data_c[val]['content']
            status = self.data_c[val]['status']
            point_last = ''
            if status==0:
                self(self.go1)
                self(self.go2,username)

                if self.driver.session_id is not None:
                    if 'parent' in self.data_c[val].keys():
                        reg_path = self.driver.find_elements_by_xpath(".//span[contains(text(),'"+self.data_c[val]['parent']['content']+"')]")

                        for val2 in reg_path:
                            point = val2.find_element_by_xpath("..")
                            text = str(point.text)

                            # has from_user?
                            if not from_user:
                                searchObj = re.search( r'(.*?)：[\s\S]*', text, re.M|re.I|re.U)
                                if searchObj and searchObj.group(1).strip()==to_user:
                                    point_last = point
                                    break
                            else:
                                searchObj = re.search( r'(.*) 回复 (.*?)：[\s\S]*', text, re.M|re.I|re.U)
                                if searchObj and searchObj.group(1).strip()==from_user and searchObj.group(2).strip()==to_user:
                                    point_last = point
                                    break
                        if point_last:
                            self(self.go3,content,id,point_last)
                    else:
                        self(self.go3,content,id)

                # makesure after go3 driver is quit
                if self.driver.session_id is not None:
                    self.driver.quit()

                # pickle.dump(driver.get_cookies() , open("QuoraCookies.pkl","wb"))

s = firefoxLink("http://jp.appgame.com/archives/251011.html")
s.run()