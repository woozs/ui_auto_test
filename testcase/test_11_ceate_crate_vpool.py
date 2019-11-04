#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/27 19:18
# @Author  : mrwuzs
# @Site    : 
# @File    : test_11_ceate_crate_vpool.py
# @Software: PyCharm

import time
import pytest
import allure

from public.common import mytest
from public.common import datainfo
from public.appModel import vdcAction
from public.pages import vdcPage
from public.appModel.loginAction import Login

@allure.feature("VPOOL管理")
class TestCreateVpool(mytest.MyTest):
    """测试创建vpool"""

    @allure.story("创建VPOOL")
    @pytest.mark.flaky(reruns=3)
    def test_create_vpool(self):
        vdc_a = vdcAction.VdcACction(self.dr)
        vdc_pg = vdcPage.VdcPage(self.dr)
        login = Login(self.dr)
        datas = datainfo.get_xls_to_dict("user.xlsx", "Sheet1")[0]
        p_data = datainfo.get_xls_to_dict("vdc_vpool.xlsx","Sheet1")[0]
        login.login(datas["username"], datas["password"])
        vdc_a.create_vpool(p_data["vdcname"],p_data["vpoolname"],"虚拟资源","数据中心",
                           "DC1",p_data["vpooldesc"])

        vdc_pg.open_vdc_page()
        time.sleep(1)
        vdc_pg.search_vdc(p_data["vdcname"])
        time.sleep(1)
        vdc_pg.click_az_buttun()
        time.sleep(1)
        vdc_pg.search_vpool(p_data["vpoolname"])
        #校验能查询到

        text = self.dr.get_text("xpath->//td")
        assert p_data["vpoolname"] in text


if __name__ == "__main__":
    pytest.main(["-s", "test_11_ceate_crate_vpool.py"])