#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/23 15:04
# @Author  : mrwuzs
# @Site    :
# @File    : loginaction.py
# @Software: PyCharm
import allure

from time import sleep
from public.pages import loginPage
from public.pages import basepage
from public.common import log


class Login(object):

    def __init__(self, driver):
        self.dr = driver
        self.log = log.Log()

    @allure.step("登录系统")
    def login(self, username, password):

        try:
            with allure.step("登录系统"):
                allure.attach("用户名:%s" % username)
                allure.attach("密码:%s" % password)
                allure.attach("验证码:1234")

            login = loginPage.LoginPage(self.dr)
            self.dr.wait(10)
            login.into_cmp_page()
            sleep(0.5)
            login.input_username(username)
            sleep(0.5)
            login.input_password(password)
            sleep(0.5)
            login.input_code(1234)
            sleep(0.5)
            login.click_loginbutton()
        except Exception as e:
            raise e

    @allure.step("退出系统")
    def logout(self):
        self.dr.origin_driver.delete_all_cookies()




if __name__ == '__main__':
    import json
    from public.common import pyselenium
    from config import globalparam
    dr = pyselenium.PySelenium(globalparam.browser)
    dr.max_window()
    login = Login(dr).login("上海管理员", "1qaz!QAZ")
    cookies = dr.origin_driver.get_cookies()
    jsonCookies = json.dumps(cookies)
    with open('cookies.json', 'w') as f:
        f.write(jsonCookies)
