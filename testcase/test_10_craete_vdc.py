#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/27 19:16
# @Author  : mrwuzs
# @Site    :
# @File    : test_10_craete_vdc.py
# @Software: PyCharm

import pytest
import allure

from public.common import mytest
from public.common import datainfo
from public.appModel import vdcAction
from public.pages import vdcPage
from public.appModel.loginAction import Login


@allure.feature("VDC管理")
class TestCreateVDC(mytest.MyTest):
    """测试创建VDC"""

    @allure.story("创建vdc")
    @pytest.mark.flaky(reruns=3)
    def test_create_vdc(self):
        vdc_a = vdcAction.VdcACction(self.dr)
        vdc_pg = vdcPage.VdcPage(self.dr)
        login = Login(self.dr)
        datas = datainfo.get_xls_to_dict("user.xlsx", "Sheet1")["创建域管理员"]
        p_data = datainfo.get_xls_to_dict("vdc_vpool.xlsx", "vdc")["创建vdc"]
        login.login(datas["username"], datas["password"])
        vdc_a.ceate_vdc(p_data["vdcname"])
        vdc_pg.open_vdc_page()
        vdc_pg.search_vdc(p_data["vdcname"])
        # 校验能查询到
        self.dr.wait(5)
        self._add_image("创建vdc")
        text = self.dr.get_text(
            "xpath->//div[@class='box-body']/table-component/div/table/tbody")
        assert p_data["vdcname"] in text


if __name__ == "__main__":
    pytest.main(["-s", "test_10_craete_vdc.py"])
