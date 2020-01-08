#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/30 9:07
# @Author  : mrwuzs
# @Site    :
# @File    : test_14_delete_tenant_user.py
# @Software: PyCharm
import pytest
import allure

from public.common.publicfunction import *
from public.common import datainfo
from public.appmodel import useraction
from public.pages import authUserPage
from public.appmodel.loginaction import Login


@allure.feature("用户管理")
class TestDeleteUser():
    """删除运营部门下的用户测试"""

    @allure.story("删除运营部门下的用户")
    @pytest.mark.flaky(reruns=3)
    def test_delete_tenant_user(self,login_domain):
        dr = login_domain
        data1s = datainfo.get_xls_to_dict("user.xlsx", "authuser")["创建运营部门用户"]
        aupg = authUserPage.AuthUsertPage(dr)
        ta = useraction.UserAction(dr)
        ta.delete_tenant_user(data1s["username"])
        aupg.open_authuser()

        aupg.input_select_user(data1s["username"])
        dr.wait(5)
        add_image(dr,"删除运营部门下的用户")
        flag = dr.element_exist("xpath->//td")
        assert flag is False

if __name__ == "__main__":
    pytest.main(["-s", "test_14_delete_tenant_user.py"])
