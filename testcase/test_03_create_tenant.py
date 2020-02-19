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
from public.common.publicfunction import *
from public.common import datainfo
from public.appmodel import tenantaction
from public.pages import auth_tenant_page

@allure.feature("运营部门管理")
class TestTeant():
    """创建运营部门"""

    @allure.story("创建运营部门")
    @pytest.mark.flaky(reruns=3)
    def test_create(self,login_domain):
        dr = login_domain
        t_data = datainfo.get_xls_to_dict("tenantdata.xlsx", "Sheet1")["创建运营部门"]
        tpg = auth_tenant_page.AuthTenantPage(dr)
        ta = tenantaction.TenantAction(dr)
        ta.create_tenant(
            t_data["tenantname"],
            t_data["linkmanname"],
            t_data["linkmanphoneno"])
        tpg.open_authtenant()
        # 搜索运营部门
        time.sleep(2)
        tpg.input_secrch_tenant(t_data["tenantname"])
        time.sleep(1)
        a = dr.get_text("id->card")
        add_image(dr,"创建运营部门")
        assert t_data["tenantname"] in a, "%s不在预期结果%s中" % (
            t_data["tenantname"], a)
        assert t_data["linkmanname"]in a, "%s不在预期结果%s中" % (
            t_data["linkmanname"], a)
        assert t_data["linkmanphoneno"]in a, "%s不在预期结果%s中" % (
            t_data["linkmanphoneno"], a)


if __name__ == "__main__":
    pytest.main(["-s", "test_03_create_tenant.py"])
