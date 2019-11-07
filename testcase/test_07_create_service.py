#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/27 19:15
# @Author  : mrwuzs
# @Site    :
# @File    : test_07_create_service.py
# @Software: PyCharm

import time
import pytest
import allure

from public.common import mytest
from public.common import datainfo
from public.appModel import resNodeAction
from public.pages import sys_regionMgrPage
from public.appModel.loginAction import Login
from public.common import pyselenium
from config import globalparam
from public.common.log import Log


@allure.feature("资源节点管理")
class TestCreateService(mytest.MyTest):
    """测试添加service"""

    def setup_class(self):
        """重写方法"""
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

    @allure.story("创建VMware服务")
    @pytest.mark.flaky(reruns=5)
    def test_create_service_vmware(self):
        p_data = datainfo.get_xls_to_dict("res_node_data.xlsx", "vmwareapi")[0]
        self.arn.add_resource_service_node_vmware(
            p_data["regionname"],
            p_data["nodename"],
            p_data["servicename"],
            p_data["servicetype"],
            p_data["username"],
            p_data["passwrd"])
        # 校验
        self.srmpg.open_sys_regionMgr_page()
        # time.sleep(1)
        # self.srmpg.click_region_tree(p_data["regionname"])
        # self.srmpg.click_tree_res_node(p_data["nodename"])
        # self.srmpg.click_tree_res_node_i(p_data["nodename"])

        flag = self.dr.element_exist(
            "xpath->(//a[contains(text(),'%s')])" %
            p_data["servicename"])
        assert flag

    @allure.story("创建opentack服务")
    @pytest.mark.flaky(reruns=5)
    def test_create_service_openstack(self):
        p_data = datainfo.get_xls_to_dict(
            "res_node_data.xlsx", "openstackapi")[0]
        self.arn.add_resource_service_node_vmware(
            p_data["regionname"],
            p_data["nodename"],
            p_data["servicename"],
            p_data["servicetype"],
            p_data["username"],
            p_data["passwrd"])
        # 校验
        self.srmpg.open_sys_regionMgr_page()

        flag = self.dr.element_exist(
            "xpath->(//a[contains(text(),'%s')])" %
            p_data["servicename"])
        assert flag


if __name__ == "__main__":
    pytest.main(["-s", "test_07_create_service.py"])
