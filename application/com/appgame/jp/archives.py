#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import pickle
import sys
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def gg():
    print 'hello'

# reload(sys)
# sys.setdefaultencoding('utf-8')
# try:
#     # driver = webdriver.Firefox()
#     driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',desired_capabilities=DesiredCapabilities.FIREFOX)
#
#     # driver.set_window_size(1080,300)
#     driver.get("http://jp.appgame.com/archives/259320.html")
#     time.sleep(5)
#     js="var q=document.documentElement.scrollTop=2200"
#     driver.execute_script(js)
#     time.sleep(3)
#     driver.switch_to.frame(driver.find_element_by_id("commentics-iframe"))
#     #To continue with the default content do
#     # driver.switch_to.default_content()
#     driver.find_element_by_css_selector("a.sso_login").click()
#     time.sleep(5)
#     driver.find_element_by_id("email").clear()
#     driver.find_element_by_id("email").send_keys("demo")
#     driver.find_element_by_id("password").clear()
#     driver.find_element_by_id("password").send_keys("demo")
#     driver.find_element_by_link_text(u"登录").click()
#     time.sleep(5)
#
#     driver.switch_to.frame(driver.find_element_by_id("commentics-iframe"))
#     driver.find_element_by_name("cmtx_comment").clear()
#     driver.find_element_by_name("cmtx_comment").send_keys("hi2")
#     driver.find_element_by_link_text(u"评论").click()
#     time.sleep(5)
#     # pickle.dump(driver.get_cookies() , open("QuoraCookies.pkl","wb"))
#     driver.quit()
# except:
#     driver.quit()

