__author__ = 'dingxinhui'
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# encapsulation/encapsulation.py

# 封装部分维护在此
import os
from config.config_01 import locat_config
from log.log import Logger
from selenium.webdriver.support.wait import WebDriverWait
from picture.picture import insert_img
from selenium.webdriver.support import expected_conditions as EC

class UIHandle():
    logger = Logger()

    # 构造方法，用来接收selenium的driver对象
    @classmethod
    def __init__(cls, driver):
        cls.driver = driver

    # 输入地址
    @classmethod
    def get(cls, url):
        cls.logger.loginfo(url)
        cls.driver.get(url)

    # 关闭浏览器驱动
    @classmethod
    def quit(cls):
        cls.driver.quit()

    # element对象（还可加入try，截图等。。。）
    @classmethod
    def element(cls, page, element):
        # 加入日志
        cls.logger.loginfo(page)
        # 加入隐性等待
        # 此处便可以传入config_o1中的dict定位参数
        try:
            el = WebDriverWait(cls.driver, 30).until(EC.presence_of_element_located(locat_config[page][element]))
            #  加入日志
            cls.logger.loginfo(page+'OK')
            print("页面‘" + page + "’和元素‘" + element + "’ was found")
            return el
        except:
            print("元素没有找到")
            return insert_img(cls.driver, '找不到元素.png')
        # 加入日志
        cls.logger.loginfo(page+'OK')
        return el
    # element对象(还未完成。。。)
    def elements(cls, page, element):
        # 加入日志
        cls.logger.loginfo(page)
        # 加入隐性等待
        WebDriverWait(cls.driver, 10)
        els = cls.driver.find_elements(*locat_config[page][element])
        # 注意返回的是list
        return els

    # send_keys方法
    @classmethod
    def Input(cls, page, element, msg):
        el = cls.element(page, element)
        el.send_keys(msg)

    # click方法
    @classmethod
    def Click(cls, page, element):
        el = cls.element(page, element)
        el.click()

    @classmethod
    def setUp(self):
       self.imgs = []
       self.addCleanup(self.cleanup)
