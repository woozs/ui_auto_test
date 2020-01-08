#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/25 18:01
# @Author  : mrwuzs
# @Site    :
# @File    : test_04_create_auth_user.py
# @Software: PyCharm
import pytest
import allure

from public.common.publicfunction import *
from public.common import datainfo
from public.appmodel import useraction
from public.pages import authUserPage



@allure.feature("用户管理")
class TestCreateUser():
    """创建运营部门下的用户测试"""

    @allure.story("创建运营部门下的用户")
    @pytest.mark.flaky(reruns=3)
    def test_create_authuser(self,login_domain):
        dr = login_domain
        data1s = datainfo.get_xls_to_dict("user.xlsx", "authuser")["创建运营部门用户"]
        aupg = authUserPage.AuthUsertPage(dr)
        ta = useraction.UserAction(dr)
        ta.create_tenant_user(
            data1s["tenantname"],
            data1s["username"],
            data1s["firstname"],
            data1s["password"],
            data1s["repassword"],
            data1s["email"])
        aupg.open_authuser()
        aupg.input_select_user(data1s["username"])
        dr.wait(5)
        add_image(dr,"创建运营部门下的用户")
        text = dr.get_text(
            "xpath->//div[@class='box-body']/table-component/div/table/tbody")

        assert data1s["username"] in text, "%s不在预期结果%s中" % (
            data1s["username"], text)
        assert data1s["firstname"] in text, "%s不在预期结果%s中" % (
            data1s["firstname"], text)
        assert data1s["email"] in text, "%s不在预期结果%s中" % (data1s["email"], text)


if __name__ == "__main__":
    pytest.main(["-s", "test_04_create_auth_user.py"])
