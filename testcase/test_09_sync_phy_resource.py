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

from public.common import mytest
from public.common import datainfo
from public.appModel import resSyncAction
from public.pages import resSyncPage

@allure.feature("资源同步")
class TestPhySunc(mytest.MyTest):
    """物理资源同步"""

    @allure.story("同步物理资源")
    @pytest.mark.flaky(reruns=3)
    def test_sync_phy_res(self):
        datas = datainfo.get_xls_to_dict("user.xlsx", "Sheet1")[0]
        p_data = datainfo.get_xls_to_dict("res_node_data.xlsx", "region")[0]

        self.login.login(datas["username"], datas["password"])
        sync_a =  resSyncAction.ResSync(self.dr)
        sync_pg = resSyncPage.ResSyncPage(self.dr)
        sync_a.phy_res_sync(p_data["regionname"],p_data["nodename"],"DC1","DC2")
        # sync_a.phy_res_sync("北京","")
        time.sleep(20)
        #延时，等待同步完成
        # self.dr.F5()
        # sync_pg.open_osphysicalsyncpage()
        sync_pg.click_refresh_button()
        status1 = self.dr.get_text("xpath->//td[contains(.,'DC1')]/../td[3]").strip()
        count1 = 0
        while status1 == "执行中":
            time.sleep(10)
            sync_pg.click_refresh_button()
            status1 = self.dr.get_text("xpath->//td[contains(.,'DC1')]/../td[3]").strip()
            count1 += 1
            if count1 == 10:
                break
        assert status1 == "执行成功"
        status2 = self.dr.get_text("xpath->//td[contains(.,'DC2')]/../td[3]").strip()
        count2 = 0
        while status2 == "执行中":
            time.sleep(10)
            sync_pg.click_refresh_button()
            status2 = self.dr.get_text("xpath->//td[contains(.,'DC1')]/../td[3]").strip()
            count2 += 1
            if count2 == 10:
                break
        assert status2 == "执行成功"




if __name__ == "__main__":
    pytest.main(["-s", "test_09_sync_phy_resource.py"])