#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/30 10:44
# @Author  : mrwuzs
# @Site    :
# @File    : test_16_delete_tenant.py
# @Software: PyCharm
import pytest
from public.common.publicfunction import *
from public.common import datainfo
from public.appmodel import tenantaction
from public.pages import auth_tenant_page
from public.appmodel.loginaction import Login


@allure.feature("运营部门管理")
class TestTenantDelete():
    """删除运营部门测试"""
    @allure.story("删除运营部门")
    @pytest.mark.flaky(reruns=3)
    def test_delete_tenant(self,login_admin):
        dr = login_admin
        t_data = datainfo.get_xls_to_dict("tenantdata.xlsx", "Sheet1")["创建运营部门"]
        tpg = auth_tenant_page.AuthTenantPage(dr)
        ta = tenantaction.TenantAction(dr)
        try:
            ta.remove_post(t_data["tenantname"])
        except BaseException:
            self.logger.error("移除用户失败，请确认是否该岗位未关联用户")
        ta.delete_tenant(t_data["tenantname"])
        tpg.open_authtenant()
        # 搜索运营部门
        tpg.input_secrch_tenant(t_data["tenantname"])
        time.sleep(2)
        dr.wait(5)
        add_image(dr,"删除运营部门")
        flag = dr.element_exist("id->card")
        assert flag is False


if __name__ == "__main__":
    pytest.main(["-s", "test_16_delete_tenant.py"])
