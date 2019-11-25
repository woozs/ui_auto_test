#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/30 9:04
# @Author  : mrwuzs
# @Site    :
# @File    : test_13_delete_vdc.py
# @Software: PyCharm

import time
import pytest
import allure

from public.common import mytest
from public.appModel import vdcAction
from public.pages import vdcPage
from public.common import datainfo


@allure.feature("VDC管理")
class Test_Vpool_Vdc(mytest.MyTest):
    """测试删除VDC"""

    @allure.story("删除VDC")
    @pytest.mark.flaky(reruns=3)
    def test_delete_vdc(self):
        vdc_a = vdcAction.VdcACction(self.dr)
        vdc_pg = vdcPage.VdcPage(self.dr)

        p_data = datainfo.get_xls_to_dict("vdc_vpool.xlsx", "vdc")["创建vdc"]

        self.login.login("系统管理员", "123456")
        vdc_a.delete_vdc(p_data["vdcname"])
        vdc_pg.open_vdc_page()
        time.sleep(1)
        vdc_pg.search_vdc(p_data["vdcname"])

        #         # 校验能查询到
        self.dr.wait(5)
        self._add_image("删除VDC")
        flag = self.dr.element_exist("xpath->//td")
        assert flag is False


if __name__ == "__main__":
    pytest.main(["-s", "test_13_delete_vdc.py"])
