#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/25 17:12
# @Author  : mrwuzs
# @Site    :
# @File    : test_03_create_tenant.py
# @Software: PyCharm


import time
import pytest
import allure
from public.common import publicfunction
from public.common import mytest
from public.common import datainfo
from public.appModel import tenantAction
from public.pages import authTenantPage
from public.appModel.loginAction import Login


@allure.feature("运营部门管理")
class TestTeant(mytest.MyTest):
    """创建运营部门"""

    @allure.story("创建运营部门")
    @pytest.mark.flaky(reruns=3)
    def test_create(self):

        login = Login(self.dr)
        datas = datainfo.get_xls_to_dict("user.xlsx", "Sheet1")["创建域管理员"]
        t_data = datainfo.get_xls_to_dict("tenantdata.xlsx", "Sheet1")["创建运营部门"]
        tpg = authTenantPage.AuthTenantPage(self.dr)
        ta = tenantAction.TenantAction(self.dr)
        # login.login("wuzs0001","1qaz!QAZ")
        login.login(datas["username"], datas["password"])
        ta.create_tenant(
            t_data["tenantname"],
            t_data["linkmanname"],
            t_data["linkmanphoneno"])
        tpg.open_authtenant()
        # 搜索运营部门
        time.sleep(2)
        tpg.input_secrch_tenant(t_data["tenantname"])
        time.sleep(1)
        a = self.dr.get_text("id->card")
        self._add_image("创建运营部门")
        assert t_data["tenantname"] in a, "%s不在预期结果%s中" % (
            t_data["tenantname"], a)
        assert t_data["linkmanname"]in a, "%s不在预期结果%s中" % (
            t_data["linkmanname"], a)
        assert t_data["linkmanphoneno"]in a, "%s不在预期结果%s中" % (
            t_data["linkmanphoneno"], a)


if __name__ == "__main__":
    pytest.main(["-s", "test_03_create_tenant.py"])
