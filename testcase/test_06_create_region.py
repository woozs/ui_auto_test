#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/25 18:55
# @Author  : mrwuzs
# @Site    :
# @File    : test_06_create_region.py
# @Software: PyCharm

import pytest
import time
import allure

from public.common import mytest
from public.common import datainfo
from public.appModel import resNodeAction
from public.pages import sys_regionMgrPage
from public.appModel.loginAction import Login


@allure.feature("资源节点管理")
class TestCreateRegion(mytest.MyTest):
    """测试添加资源节点"""

    @allure.story("创建资源节点")
    @pytest.mark.flaky(reruns=3)
    def test_create_region(self):

        login = Login(self.dr)
        datas = datainfo.get_xls_to_dict("user.xlsx", "Sheet1")[0]
        p_data = datainfo.get_xls_to_dict("res_node_data.xlsx", "region")[0]

        arn = resNodeAction.Add_Res_Node(self.dr)
        srmpg = sys_regionMgrPage.SysRegionMgrPage(self.dr)
        # login.login("wuzs0001","1qaz!QAZ")
        login.login(datas["username"], datas["password"])

        arn.add_res_node(
            p_data["regionname"],
            p_data["nodename"],
            business_type=p_data["business_type"],
            platform=p_data["platform"],
            virtual_type=p_data["virtual_type"],
            regDesc=p_data["regDesc"])


        srmpg.open_sys_regionMgr_page()
        time.sleep(1)
        self.dr.wait(5)
        self._add_image("创建资源节点")
        flag = self.dr.element_exist(
            "xpath->//a[contains(text(),'%s')]" %
            p_data["nodename"])
        assert flag, "未查询到资源节点%s" % p_data["nodename"]


if __name__ == "__main__":
    pytest.main(["-s", "test_06_create_region.py"])
