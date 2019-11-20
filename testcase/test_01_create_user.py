#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/25 11:05
# @Author  : mrwuzs
# @Site    :
# @File    : test_01_create_user.py
# @Software: PyCharm

import pytest
import allure

from time import sleep
from public.common import mytest
from public.common import datainfo
from public.appModel import userAction
from public.pages import sysUorgMgrPage
from public.appModel.loginAction import Login
from public.common import publicfunction


@allure.feature("用户管理")
class TestCreateUser(mytest.MyTest):
    """创建用户"""

    @allure.story("创建用户")
    @pytest.mark.flaky(reruns=3)
    def test_create_user(self):

        login = Login(self.dr)
        login.login("系统管理员", '123456')

        datas = datainfo.get_xls_to_dict("user.xlsx", "Sheet1")[0]
        upage = sysUorgMgrPage.SysUorgMgrPage(self.dr)
        ua = userAction.UserAction(self.dr)

        ua.create_user(
            datas["mgrname"],
            datas["username"],
            datas["firstname"],
            datas["password"],
            datas["repassword"],
            datas["email"])
        # upage.input_select_user(datas["username"])
        # 查看用户，进行校验
        upage.input_select_user(datas["username"])
        self._add_image("创建用户")
        assert self.dr.element_exist(
            "xpath->//span[contains(.,'%s')]" %
            datas["username"])



if __name__ == "__main__":
    pytest.main(["-s", "test_01_create_user.py"])
