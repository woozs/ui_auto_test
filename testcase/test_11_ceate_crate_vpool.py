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

from public.common.publicfunction import *
from public.common import datainfo
from public.appmodel import vdcaction
from public.pages import vdcPage
from public.appmodel.loginaction import Login


@allure.feature("VPOOL管理")
class TestCreateVpool():
    """测试创建vpool"""

    @allure.story("创建VPOOL")
    @pytest.mark.flaky(reruns=3)
    def test_create_vpool(self,login_domain):
        dr = login_domain
        vdc_a = vdcaction.VdcACction(dr)
        vdc_pg = vdcPage.VdcPage(dr)
        p_data = datainfo.get_xls_to_dict("vdc_vpool.xlsx", "vpool")["创建vpool"]
        vdc_a.create_vpool(
            p_data["vdcname"],
            p_data["vpoolname"],
            "虚拟资源",
            "数据中心",
            "DC1",
            p_data["vpooldesc"])

        vdc_pg.open_vdc_page()
        time.sleep(1)
        vdc_pg.search_vdc(p_data["vdcname"])
        time.sleep(1)
        vdc_pg.click_az_buttun()
        time.sleep(1)
        vdc_pg.search_vpool(p_data["vpoolname"])
        # 校验能查询到
        dr.wait(5)
        add_image(dr,"创建VPOOL")
        text = dr.get_text("xpath->//td")
        assert p_data["vpoolname"] in text


if __name__ == "__main__":
    pytest.main(["-s", "test_11_ceate_crate_vpool.py"])
