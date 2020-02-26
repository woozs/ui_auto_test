#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/30 9:04
# @Author  : mrwuzs
# @Site    :
# @File    : test_13_delete_vdc.py
# @Software: PyCharm

import pytest

from public.common.publicfunction import *
from public.appmodel import vdcaction
from public.pages import vdcPage
from public.common import datainfo


@allure.feature("VDC管理")
class Test_Vpool_Vdc():
    """测试删除VDC"""

    @allure.story("删除VDC")
    @pytest.mark.flaky(reruns=globalparam.RENUM)
    def test_delete_vdc(self,login_domain):
        dr = login_domain
        vdc_a = vdcaction.VdcACction(dr)
        vdc_pg = vdcPage.VdcPage(dr)
        p_data = datainfo.get_xls_to_dict("vdc_vpool.xlsx", "vdc")["创建vdc"]
        vdc_a.delete_vdc(p_data["vdcname"])
        vdc_pg.open_vdc_page()
        time.sleep(globalparam.small)
        vdc_pg.search_vdc(p_data["vdcname"])
        #         # 校验能查询到
        dr.wait(5)
        add_image(dr,"删除VDC")
        flag = dr.element_exist("xpath->//td")
        assert flag is False


if __name__ == "__main__":
    pytest.main(["-s", "test_13_delete_vdc.py"])
