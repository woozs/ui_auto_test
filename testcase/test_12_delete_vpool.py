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

from public.common import mytest
from public.appModel import vdcAction
from public.pages import vdcPage
from public.common import datainfo


@allure.feature("VPOOL管理")
class Test_Vpool_Delete(mytest.MyTest):
    """测试删除vpool"""

    @allure.story("删除VPOOL")
    @pytest.mark.flaky(reruns=3)
    def test_delete_vpool(self):
        vdc_a = vdcAction.VdcACction(self.dr)
        vdc_pg = vdcPage.VdcPage(self.dr)

        p_data = datainfo.get_xls_to_dict("vdc_vpool.xlsx", "Sheet1")[0]

        self.login.login("系统管理员", "123456")
        vdc_a.delete_vpool(p_data["vdcname"], p_data["vpoolname"])
        vdc_pg.open_vdc_page()
        time.sleep(1)
        vdc_pg.search_vdc(p_data["vdcname"])
        vdc_pg.click_az_buttun()
        time.sleep(1)
        vdc_pg.search_vpool(p_data["vpoolname"])
        # 校验能查询到

        flag = self.dr.element_exist("xpath->//td")
        assert flag is False


if __name__ == "__main__":
    pytest.main(["-s", "test_12_delete_vpool.py"])
