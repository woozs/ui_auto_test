#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/30 10:44
# @Author  : mrwuzs
# @Site    : 
# @File    : test_16_delete_tenant.py
# @Software: PyCharm
import time
import pytest
import allure

from public.common import mytest
from public.common import datainfo
from public.appModel import tenantAction
from public.pages import authTenantPage
from public.appModel.loginAction import Login

@allure.feature("运营部门管理")
class TestTenantDelete(mytest.MyTest):
    """删除运营部门测试"""
    @allure.story("删除运营部门")
    @pytest.mark.flaky(reruns=3)
    def test_delete_tenant(self):
        login = Login(self.dr)
        t_data = datainfo.get_xls_to_dict("tenantdata.xlsx", "Sheet1")[0]

        tpg = authTenantPage.AuthTenantPage(self.dr)
        ta = tenantAction.TenantAction(self.dr)
        # login.login("wuzs0001","1qaz!QAZ")
        login.login("系统管理员","123456")

        try:
            ta.remove_post(t_data["tenantname"])
        except:
            print("移除用户失败，请确认是否该岗位未关联用户")
        ta.delete_tenant(t_data["tenantname"])

        tpg.open_authtenant()
        # 搜索运营部门
        tpg.input_secrch_tenant(t_data["tenantname"])
        time.sleep(2)
        flag = self.dr.element_exist("id->card")
        assert flag is False

if __name__ == "__main__":
    pytest.main(["-s", "test_16_delete_tenant.py"])