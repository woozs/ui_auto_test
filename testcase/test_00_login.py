#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/23 14:37
# @Author  : mrwuzs
# @Site    :
# @File    : test_00_login.py
# @Software: PyCharm
import pytest
import allure

from time import sleep
from public.common import mytest
from public.pages import loginPage
from public.appModel import loginAction



@allure.feature("登录模块")
class TestLoin(mytest.MyTest):
    """登录测试"""

    @allure.story("系统管理员登录系统")
    @pytest.mark.flaky(reruns=3)
    def test_login(self):
        loginpj = loginPage.LoginPage(self.dr)
        login = loginAction.Login(self.dr)
        login.login("系统管理员","123456")
        sleep(0.5)
        loginpj.click_loginbutton()
        self.dr.wait(5)
        self._add_image("系统管理员登录系统后")
        flag = self.dr.element_exist("xpath->//div[3]/div[3]/span")
        assert flag


if __name__ == "__main__":
    pytest.main(["-s", "test_00_login.py"])
