#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/23 14:37
# @Author  : mrwuzs
# @Site    :
# @File    : test_00_login.py
# @Software: PyCharm
import pytest
from  public.common.publicfunction import *

#前置条件，打开浏览器，在这个测试套下全局有效,实现在conftest.py，每个测试测试套下只打开一次浏览器
#此部分相当于setupclasss，每个测试类的setup
@allure.feature("登录模块")
class TestLoin():
    """登录测试"""
    @allure.story("系统管理员登录系统")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.flaky(reruns=globalparam.RENUM)
    def test_login(self,login_admin):
        dr = login_admin
        dr.wait(5)
        flag = dr.element_exist("xpath->//div[3]/div[3]/span")
        assert flag
        add_image(dr,"系统管理员登录系统")

if __name__ == "__main__":
    pytest.main(["-s", "test_00_login.py"])
