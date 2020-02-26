#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/30 19:05
# @Author  : mrwuzs
# @Site    :
# @File    : test_09_sync_phy_resource.py
# @Software: PyCharm

import time
import pytest
import allure

from public.common.publicfunction import *
from public.common import datainfo
from public.appmodel import ressyncaction
from public.pages import resSyncPage


@allure.feature("资源同步")
class TestPhySunc():
    """物理资源同步"""

    @allure.story("同步物理资源")
    @pytest.mark.flaky(reruns=globalparam.RENUM)
    def test_sync_phy_res(self,login_domain):
        dr = login_domain
        p_data = datainfo.get_xls_to_dict("phy_sync_data.xlsx", "Sheet1")["物理资源同步"]
        sync_a = ressyncaction.ResSync(dr)
        sync_pg = resSyncPage.ResSyncPage(dr)
        sync_a.phy_res_sync(
            p_data["regionname"],
            p_data["nodename"],
            "DC1",
            "DC2")
        time.sleep(20)
        sync_pg.click_refresh_button()
        status1 = dr.get_text(
            "xpath->//td[contains(.,'DC1')]/../td[3]").strip()
        count1 = 0
        while status1 == "执行中":
            time.sleep(10)
            sync_pg.click_refresh_button()
            status1 = dr.get_text(
                "xpath->//td[contains(.,'DC1')]/../td[3]").strip()
            count1 += 1
            if count1 == 10:
                break
        add_image(dr,"同步物理资源-DC1")
        assert status1 == "执行成功"
        status2 = dr.get_text(
            "xpath->//td[contains(.,'DC2')]/../td[3]").strip()
        count2 = 0
        while status2 == "执行中":
            time.sleep(globalparam.long)
            sync_pg.click_refresh_button()
            status2 = dr.get_text(
                "xpath->//td[contains(.,'DC1')]/../td[3]").strip()
            count2 += 1
            if count2 == 10:
                break
        add_image(dr,"同步物理资源-DC2")
        assert status2 == "执行成功"


if __name__ == "__main__":
    pytest.main(["-s", "test_09_sync_phy_resource.py"])
