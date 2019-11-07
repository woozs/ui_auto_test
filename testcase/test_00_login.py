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


@allure.feature("登录模块")
class TestLoin(mytest.MyTest):
    """登录测试"""

    # def setup_class(self):
    #     self.logger = Log()
    #     self.logger.info('############################### START ###############################')
    #     self.dr = pyselenium.PySelenium(globalparam.browser)
    #     self.dr.max_window()
    #     self.login = Login(self.dr)
    #
    # def teardown_class(self):
    #     self.dr.quit()
    # self.logger.info('###############################  End
    # ###############################')
    @allure.story("系统管理员登录系统")
    @pytest.mark.flaky(reruns=3)
    def test_login(self):
        loginpj = loginPage.LoginPage(self.dr)
        loginpj.into_cmp_page()
        loginpj.input_username("系统管理员")
        loginpj.input_password("123456")
        loginpj.input_code(1244)
        sleep(0.5)
        loginpj.click_loginbutton()

        flag = self.dr.element_exist("xpath->//div[3]/div[3]/span")
        assert flag


if __name__ == "__main__":
    pytest.main(["-s", "test_00_login.py"])
