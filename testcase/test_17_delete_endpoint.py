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

from public.common.publicfunction import *
from public.common import datainfo
from public.appmodel import resnodeaction
from public.pages import sys_regionMgrPage
from public.appmodel.loginaction import Login
from public.common import pyselenium
from config import globalparam
from public.common.log import Log


@allure.feature("资源节点管理")
class TestDeleteEndpoint():
    """测试删除Endpoint"""

    @allure.story("VMware删除endpint")
    @pytest.mark.flaky(reruns=3)
    def test_delete_vmware_endpoint(self,login_domain):
        """
        测试删除vmware，endpoint
        :return:
        """
        dr = login_domain
        self.arn = resnodeaction.Add_Res_Node(dr)
        self.srmpg = sys_regionMgrPage.SysRegionMgrPage(dr)
        p_data = datainfo.get_xls_to_dict("res_node_data.xlsx", "endpoint")[
            "创建vmware-endpoint"]
        self.arn.delete_endpoint(
            p_data["regionname"],
            p_data["nodename"],
            p_data["servicename"])
        time.sleep(1)
        dr.wait(5)
        add_image(dr,"VMware删除endpint")
        flag = dr.element_exist(
            "xpath->//table[@id='accessPoint']/tbody/tr[2]")
        assert flag is False

    @allure.story("openstack删除endpoint")
    @pytest.mark.flaky(reruns=3)
    def test_delete_openstack_endpoint(self,login_domain):
        """
        测试删除openstack，endpoint
        :return:
        """
        dr = login_domain
        self.arn = resnodeaction.Add_Res_Node(dr)
        self.srmpg = sys_regionMgrPage.SysRegionMgrPage(dr)
        p_data = datainfo.get_xls_to_dict(
            "res_node_data.xlsx", "endpoint")["创建os-l-endpoint"]
        self.arn.delete_endpoint(
            p_data["regionname"],
            p_data["nodename"],
            p_data["servicename"])
        time.sleep(1)
        dr.wait(5)
        add_image(dr,"openstack删除endpoint")
        flag = dr.element_exist(
            "xpath->//table[@id='accessPoint']/tbody/tr[2]")
        assert flag is False


if __name__ == "__main__":
    pytest.main(["-s", "test_17_delete_endpoint.py"])
