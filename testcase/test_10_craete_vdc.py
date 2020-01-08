#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/27 19:16
# @Author  : mrwuzs
# @Site    :
# @File    : test_10_craete_vdc.py
# @Software: PyCharm

import pytest
import allure

from public.common.publicfunction import *
from public.common import datainfo
from public.appmodel import vdcaction
from public.pages import vdcPage
from public.appmodel.loginaction import Login


@allure.feature("VDC管理")
class TestCreateVDC():
    """测试创建VDC"""

    @allure.story("创建vdc")
    @pytest.mark.flaky(reruns=3)
    def test_create_vdc(self,login_domain):
        dr = login_domain
        vdc_a = vdcaction.VdcACction(dr)
        vdc_pg = vdcPage.VdcPage(dr)
        p_data = datainfo.get_xls_to_dict("vdc_vpool.xlsx", "vdc")["创建vdc"]
        vdc_a.ceate_vdc(p_data["vdcname"])
        vdc_pg.open_vdc_page()
        vdc_pg.search_vdc(p_data["vdcname"])
        # 校验能查询到
        dr.wait(5)
        add_image(dr,"创建vdc")
        text = dr.get_text(
            "xpath->//div[@class='box-body']/table-component/div/table/tbody")
        assert p_data["vdcname"] in text


if __name__ == "__main__":
    pytest.main(["-s", "test_10_craete_vdc.py"])
