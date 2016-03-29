#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time

import sys
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


reload(sys)
sys.setdefaultencoding('utf-8')



try:
    # driver = webdriver.Firefox()
    driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',desired_capabilities=DesiredCapabilities.FIREFOX)


    # dcap = dict(DesiredCapabilities.PHANTOMJS)
    # dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) " +
    # "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36")
    # driver = webdriver.PhantomJS(desired_capabilities=dcap)


    # driver.set_window_size(1080,300)
    driver.get("http://jp.appgame.com/archives/259320.html")
    time.sleep(5)




    # gg = driver.find_elements_by_xpath('//*[@id="cmtx_perm_36243"]/span')
    # gg = driver.find_elements_by_xpath("//span[contains(text(),'hi2')]")

    # val = re.findall('Vitaminmin[\S\s]*?h2', driver.get_html_source())





    # js="var q=document.documentElement.scrollTop=2200"
    # driver.execute_script(js)
    # time.sleep(3)
    driver.switch_to.frame(driver.find_element_by_id("commentics-iframe"))
    #To continue with the default content do
    # driver.switch_to.default_content()

    driver.find_element_by_css_selector("a.sso_login").click()
    time.sleep(5)
    driver.find_element_by_id("email").clear()
    driver.find_element_by_id("email").send_keys("RosaRita")
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys("111111")
    driver.find_element_by_link_text(u"登录").click()
    time.sleep(5)

    driver.switch_to.frame(driver.find_element_by_id("commentics-iframe"))

    gg = driver.find_elements_by_xpath(".//span[contains(text(),'hi5')]")
    point = gg[0].find_element_by_xpath("..")
    point.find_element_by_css_selector("a.cmtx_reply_enabled").click()

    point.find_element_by_name("cmtx_comment").clear()
    point.find_element_by_name("cmtx_comment").send_keys("hi6")
    point.find_element_by_link_text(u"评论").click()
    # driver.find_element_by_name("cmtx_comment").clear()
    # driver.find_element_by_name("cmtx_comment").send_keys("hi2")
    # driver.find_element_by_link_text(u"评论").click()
    time.sleep(5)
    # pickle.dump(driver.get_cookies() , open("QuoraCookies.pkl","wb"))
    driver.quit()
except:
    driver.quit()



