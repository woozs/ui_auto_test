#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/7 14:21
# @Author  : mrwuzs
# @Site    :
# @File    : conftest.py
# @Software: PyCharm
"""
conftest.py 全局变量，主要实现以下功能：
1、添加命令行参数broswer， 用于切换不用浏览器
2、全局参数driver调用
"""


import time
import pytest
from public.common import pyselenium
from public.common import datainfo
from public.appmodel import loginaction
from config import globalparam
from public.common import log

domain_data = datainfo.get_xls_to_dict("user.xlsx", "Sheet1")["创建域管理员"]
user_data = datainfo.get_xls_to_dict("user.xlsx", "authuser")['创建运营部门用户']
log = log.Log()

@pytest.fixture(scope="session")
def driver(request):
    global driver
    '''只打开浏览器和关闭浏览器'''
    log.info("打开浏览器")
    driver = pyselenium.PySelenium(globalparam.browser)
    driver.max_window()  # 最大化

    def end():
        log.info("用例全部执行完毕，关闭浏览器")
        time.sleep(1)
        driver.quit()

    request.addfinalizer(end)
    return driver


@pytest.fixture()
def login_admin(request, driver):
    """系统管理员登录"""
    log.info("系统管理员登录")
    login = loginaction.Login(driver)
    login.login('系统管理员', '123456')

    def end():
        log.info("测试用例执行完成，登出系统")
        driver.origin_driver.delete_all_cookies()

    request.addfinalizer(end)
    return driver


@pytest.fixture()
def login_domain(request, driver):
    """域管理员登录"""
    log.info("域管理员:%s登录" % domain_data["username"])
    login = loginaction.Login(driver)
    login.login(domain_data["username"], domain_data["password"])

    def end():
        log.info("测试用例执行完成，登出系统")
        driver.origin_driver.delete_all_cookies()

    request.addfinalizer(end)
    return driver


@pytest.fixture()
def login_user(request, driver):
    """用户登录"""

    log.info("用户登录:%s登录" % domain_data["username"])
    login = loginaction.Login(driver)
    login.login(user_data["username"], user_data["password"])

    def end():
        log.info("测试用例执行完成，登出系统")
        driver.origin_driver.delete_all_cookies()

    request.addfinalizer(end)
    return driver


