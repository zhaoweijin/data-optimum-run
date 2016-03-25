#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import pickle
import sys

import os

# Insert project root path to sys.path
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../'))
if project_path not in sys.path:
    sys.path.insert(0, project_path)

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from application import create_app
from application.models import WpDataoptimumRecord

reload(sys)
sys.setdefaultencoding('utf-8')




def firefoxLink1(url,email,password):

    # os.environ['MODE'] = 'TESTING'
    app = create_app()
    with app.app_context():
        me = WpDataoptimumRecord.query.filter((WpDataoptimumRecord.state==1)).first()
        print me.url,me.times

    try:
        # driver = webdriver.Firefox()
        driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',desired_capabilities=DesiredCapabilities.FIREFOX)

        # driver.set_window_size(1080,300)
        driver.get(url)
        time.sleep(3)
        # js="var q=document.documentElement.scrollTop=2200"
        # driver.execute_script(js)
        # time.sleep(3)
        driver.switch_to.frame(driver.find_element_by_id("commentics-iframe"))
        #To continue with the default content do
        # driver.switch_to.default_content()
        driver.find_element_by_css_selector("a.sso_login").click()
        time.sleep(5)
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys(email)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(password)
        driver.find_element_by_link_text(u"登录").click()
        time.sleep(5)

        driver.switch_to.frame(driver.find_element_by_id("commentics-iframe"))

        reg_path = driver.find_elements_by_xpath(".//span[contains(text(),'hi5')]")
        point = reg_path[0].find_element_by_xpath("..")
        point.find_element_by_css_selector("a.cmtx_reply_enabled").click()

        point.find_element_by_name("cmtx_comment").clear()
        point.find_element_by_name("cmtx_comment").send_keys("hi6")
        point.find_element_by_link_text(u"评论").click()

        # driver.find_element_by_name("cmtx_comment").clear()
        # driver.find_element_by_name("cmtx_comment").send_keys("hi2")
        # driver.find_element_by_link_text(u"评论").click()
        # time.sleep(5)
        # pickle.dump(driver.get_cookies() , open("QuoraCookies.pkl","wb"))
        driver.quit()
    except:
        driver.quit()

