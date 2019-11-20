#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/27 20:24
# @Author  : mrwuzs
# @Site    :
# @File    : test_08_create_endpoint.py
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
class TestCreateEndpoint(mytest.MyTest):
    """测试添加Endpoint"""

    def setup_class(self):

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

    @allure.story("VMware创建endpoint")
    @pytest.mark.flaky(reruns=3)
    def test_vmware_endpoint(self):
        """
        测试添加vmware，endpoint
        依赖已添加vmware服务
        :return:
        """

        p_data = datainfo.get_xls_to_dict("res_node_data.xlsx", "endpoint")[1]
        self.arn.add_endpoint(
            p_data["regionname"],
            p_data["nodename"],
            p_data["servicename"],
            p_data["url"])

        time.sleep(0.5)
        self.dr.wait(5)
        self._add_image("VMware创建endpoint")
        text = self.dr.get_text(
            "xpath->//table[@id='accessPoint']/tbody/tr[2]")
        assert p_data["url"] in text

    @allure.story("openstack创建endpoint")
    @pytest.mark.flaky(reruns=3)
    def test_openstack_endpoint(self):
        """
        测试添加openstack，endpoint
        依赖已添加openstack服务
        :return:
        """

        p_data = datainfo.get_xls_to_dict("res_node_data.xlsx", "endpoint")[0]
        self.arn.add_endpoint(
            p_data["regionname"],
            p_data["nodename"],
            p_data["servicename"],
            p_data["url"])

        time.sleep(0.5)
        self.dr.wait(5)
        self._add_image("openstack创建endpoint")
        text = self.dr.get_text(
            "xpath->//table[@id='accessPoint']/tbody/tr[2]")
        assert p_data["url"] in text


if __name__ == "__main__":
    pytest.main(["-s", "test_08_create_endpoint.py"])
