#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/31 9:36
# @Author  : mrwuzs
# @Site    :
# @File    : test_21_delete_user.py
# @Software: PyCharm
import pytest
import allure

from public.common.publicfunction import *
from public.common import datainfo
from public.appmodel import useraction
from public.pages import sysUorgMgrPage
from public.appmodel.loginaction import Login
from public.common import publicfunction


@allure.feature("用户管理")


class TestDeleteUser():

    """测试删除域管理员"""
    @allure.story("删除域用户")
    @pytest.mark.flaky(reruns=3)
    def test_delete_user(self,login_admin):
        dr = login_admin
        datas = datainfo.get_xls_to_dict("user.xlsx", "Sheet1")["创建域管理员"]
        upage = sysUorgMgrPage.SysUorgMgrPage(dr)
        ua = useraction.UserAction(dr)
        ua.delete_user(datas["username"])
        upage.input_select_user(datas["username"])
        dr.wait(5)
        add_image(dr,"移除域管理员")
        flag = dr.element_exist(
            "xpath->//span[contains(.,'%s')]" %
            datas["username"])
        assert flag is flag, "用户删除成功，请查看日志"

if __name__ == "__main__":
    pytest.main(["-s", "test_21_delete_user.py"])
