#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/23 15:04
# @Author  : mrwuzs
# @Site    : 
# @File    : loginAction.py
# @Software: PyCharm
import allure

from time import sleep
from  public.pages import loginPage

class Login(object):

    def __init__(self,driver):
        self.dr = driver



    def login(self, username, password):

        try:
            with allure.step("登录系统"):
                allure.attach("用户名:%s"%username)
                allure.attach("密码:%s"%password)
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



# class ShowFunName():
#     def __init__(self, func):
#         self._func = func
#
#     def __call__(self, a):
#         print('function name:', self._func.__name__)
#         return self._func(a)

if __name__ == '__main__':
    from public.common import pyselenium
    from config import globalparam
    dr = pyselenium.PySelenium(globalparam.browser)
    dr.max_window()
    login = Login(dr).login("系统管理员","123456")