#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/27 19:21
# @Author  : mrwuzs
# @Site    :
# @File    : test_12_delete_vpool.py
# @Software: PyCharm

import time
import pytest
import allure

from public.common.publicfunction import *
from public.appmodel import vdcaction
from public.pages import vdcPage
from public.common import datainfo


@allure.feature("VPOOL管理")
class Test_Vpool_Delete():
    """测试删除vpool"""
    
    @allure.story("删除VPOOL")
    @pytest.mark.flaky(reruns=3)
    def test_delete_vpool(self,login_domain):
        dr = login_domain
        vdc_a = vdcaction.VdcACction(dr)
        vdc_pg = vdcPage.VdcPage(dr)
        p_data = datainfo.get_xls_to_dict("vdc_vpool.xlsx", "vpool")["创建vpool"]
        vdc_a.delete_vpool(p_data["vdcname"], p_data["vpoolname"])
        vdc_pg.open_vdc_page()
        time.sleep(1)
        vdc_pg.search_vdc(p_data["vdcname"])
        vdc_pg.click_az_buttun()
        time.sleep(1)
        vdc_pg.search_vpool(p_data["vpoolname"])
        # 校验能查询到
        dr.wait(5)
        add_image(dr,"删除VPOOL")
        flag = dr.element_exist("xpath->//td")
        assert flag is False

if __name__ == "__main__":
    pytest.main(["-s", "test_12_delete_vpool.py"])
