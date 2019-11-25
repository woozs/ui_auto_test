#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/7 14:21
# @Author  : mrwuzs
# @Site    :
# @File    : conftest.py
# @Software: PyCharm


import pytest
import allure
from public.common import pyselenium
from config import globalparam
from public.appModel import loginAction
from public.common import datainfo
from public.pages.loginPage import LoginPage
from public.pages.authProjectPage import AuthProjectPage
from public.pages.authTenantPage import  AuthTenantPage
from public.pages.authUserPage import  AuthUsertPage
from public.pages.dataCenterPage import DataCenterPage
from public.pages.resSyncPage import ResSyncPage
from public.pages.sysMorgMgrPage import SysMorgMgrPage
from public.pages.sysUorgMgrPage import SysUorgMgrPage
from public.pages.vdcPage import VdcPage
from public.pages.sys_regionMgrPage import SysRegionMgrPage

domain_administrators= datainfo.get_xls_to_dict("user.xlsx", "Sheet1")["创建域管理员"]


@pytest.fixture(scope='class')
def ini_pages(driver):
    login_page =LoginPage(driver)
    auth_project_page = AuthProjectPage(driver)
    yield driver, login_page



@allure.step("打开浏览器")
@pytest.fixture(scope="session")
def open_browser():
    dr = pyselenium.PySelenium(globalparam.browser)
    dr.max_window()
    return dr


@allure.step("关闭浏览器")
@pytest.fixture(scope="session")
def quit_browser(dr):
    dr.quit()


@allure.step("登录系统")
@pytest.fixture(scope="module")
def login_as_admin(dr, username, password):
    loginAction.Login(dr).login("系统管理员","123456")


@allure.step("登出系统")
@pytest.fixture(scope="module")
def logout():
    pass
