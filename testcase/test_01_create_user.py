#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/25 11:05
# @Author  : mrwuzs
# @Site    :
# @File    : test_01_create_user.py
# @Software: PyCharm

import pytest
from public.common import datainfo
from public.appmodel import useraction
from public.pages import sysUorgMgrPage
from public.common.publicfunction import *

@allure.feature("用户管理")
class TestCreateUser():
    """创建用户"""
    @allure.story("创建用户")
    @pytest.mark.flaky(reruns=3)
    def test_create_user(self,login_admin):
        dr = login_admin
        datas = datainfo.get_xls_to_dict("user.xlsx", "Sheet1")["创建域管理员"]
        upage = sysUorgMgrPage.SysUorgMgrPage(dr)
        ua = useraction.UserAction(dr)
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
        add_image(dr, "创建用户")
        assert dr.element_exist(
            "xpath->//span[contains(.,'%s')]" %
            datas["username"])



if __name__ == "__main__":
    pytest.main(["-s", "test_01_create_user.py"])
