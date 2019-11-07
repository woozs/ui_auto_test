#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 200.59/0.50/30 0.50.5:0.50
# @Author  : mrwuzs
# @Site    :
# @File    : test_17_delete_endpoint.py
# @Software: PyCharm

import pytest
import allure
import time

from public.common import mytest
from public.common import datainfo
from public.appModel import resNodeAction
from public.pages import sys_regionMgrPage
from public.appModel.loginAction import Login
from public.common import pyselenium
from config import globalparam
from public.common.log import Log


@allure.feature("资源节点管理")
class TestDeleteEndpoint(mytest.MyTest):
    """测试删除Endpoint"""

    def setup_class(self):
        """重写类级setup"""
        self.logger = Log()
        self.logger.info(
            '############################### START ###############################')
        self.dr = pyselenium.PySelenium(globalparam.browser)
        self.dr.max_window()
        self.login = Login(self.dr)
        self.datas = datainfo.get_xls_to_dict("user.xlsx", "Sheet1")[0]
        self.login.login(self.datas["username"], self.datas["password"])
        self.arn = resNodeAction.Add_Res_Node(self.dr)
        self.srmpg = sys_regionMgrPage.SysRegionMgrPage(self.dr)

    @allure.story("VMware删除endpint")
    @pytest.mark.flaky(reruns=3)
    def test_delete_vmware_endpoint(self):
        """
        测试删除vmware，endpoint
        :return:
        """
        p_data = datainfo.get_xls_to_dict("res_node_data.xlsx", "endpoint")[0]
        # self.arn.add_endpoint(p_data["regionname"],p_data["nodename"],p_data["servicename"],p_data["url"])
        self.arn.delete_endpoint(
            p_data["regionname"],
            p_data["nodename"],
            p_data["servicename"])

        # self.srmpg.open_sys_regionMgr_page()
        #
        # self.srmpg.click_region_tree(p_data["regionname"])
        # time.sleep(5)
        # # self.srmpg.click_tree_res_node(p_data["nodename"])
        # self.srmpg.click_tree_res_node_i(p_data["nodename"])
        # time.sleep(0.5)
        # self.srmpg.click_tree_res_service(p_data["servicename"])
        # time.sleep(0.5)
        time.sleep(1)
        flag = self.dr.element_exist(
            "xpath->//table[@id='accessPoint']/tbody/tr[2]")
        assert flag is False

    @allure.story("openstack删除endpoint")
    @pytest.mark.flaky(reruns=3)
    def test_delete_openstack_endpoint(self):
        """
        测试删除openstack，endpoint
        :return:
        """

        p_data = datainfo.get_xls_to_dict("res_node_data.xlsx", "endpoint")[1]
        # self.arn.add_endpoint(p_data["regionname"], p_data["nodename"], p_data["servicename"], p_data["url"])
        self.arn.delete_endpoint(
            p_data["regionname"],
            p_data["nodename"],
            p_data["servicename"])

        # self.srmpg.open_sys_regionMgr_page()
        # self.srmpg.click_region_tree(p_data["regionname"])
        # time.sleep(3)
        # # self.srmpg.click_tree_res_node(p_data["nodename"])
        # self.srmpg.click_tree_res_node_i(p_data["nodename"])
        # time.sleep(0.5)
        # self.srmpg.click_tree_res_service(p_data["servicename"])
        # time.sleep(0.5)
        time.sleep(1)
        flag = self.dr.element_exist(
            "xpath->//table[@id='accessPoint']/tbody/tr[2]")
        assert flag is False


if __name__ == "__main__":
    pytest.main(["-s", "test_17_delete_endpoint.py"])
