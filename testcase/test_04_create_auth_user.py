#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/25 18:01
# @Author  : mrwuzs
# @Site    :
# @File    : test_04_create_auth_user.py
# @Software: PyCharm
import pytest
import allure

from public.common import mytest
from public.common import datainfo
from public.appModel import userAction
from public.pages import authUserPage
from public.appModel.loginAction import Login


@allure.feature("用户管理")
class TestCreateUser(mytest.MyTest):
    """创建运营部门下的用户测试"""

    @allure.story("创建运营部门下的用户")
    @pytest.mark.flaky(reruns=3)
    def test_create_authuser(self):

        login = Login(self.dr)
        datas = datainfo.get_xls_to_dict("user.xlsx", "Sheet1")[0]
        data1s = datainfo.get_xls_to_dict("user.xlsx", "authuser")[0]
        aupg = authUserPage.AuthUsertPage(self.dr)
        ta = userAction.UserAction(self.dr)
        # t_data = datainfo.get_xls_to_dict("tenantdata.xlsx","Sheet1")[0]
        login.login(datas["username"], datas["password"])
        ta.create_tenant_user(
            data1s["tenantname"],
            data1s["username"],
            data1s["firstname"],
            data1s["password"],
            data1s["repassword"],
            data1s["email"])
        aupg.open_authuser()

        aupg.input_select_user(data1s["username"])
        self.dr.wait(5)
        self._add_image("创建运营部门下的用户")
        text = self.dr.get_text(
            "xpath->//div[@class='box-body']/table-component/div/table/tbody")

        assert data1s["username"] in text, "%s不在预期结果%s中" % (
            data1s["username"], text)
        assert data1s["firstname"] in text, "%s不在预期结果%s中" % (
            data1s["firstname"], text)
        assert data1s["email"] in text, "%s不在预期结果%s中" % (data1s["email"], text)


if __name__ == "__main__":
    pytest.main(["-s", "test_04_create_auth_user.py"])
