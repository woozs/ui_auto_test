#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/30 11:43
# @Author  : mrwuzs
# @Site    :
# @File    : test_18_delete_service.py
# @Software: PyCharm

import time
import pytest
import allure

from public.common.publicfunction import *
from public.common import datainfo
from public.appmodel import resnodeaction
from public.pages import sys_regionMgrPage
from public.appmodel.loginaction import Login
from public.common import pyselenium
from config import globalparam
from public.common.log import Log


@allure.feature("资源节点管理")
class TestDeleteService():
    """测试删除service"""
    @allure.story("删除VMware服务")
    @pytest.mark.flaky(reruns=3)
    def test_delete_service_vmware(self,login_domain):
        dr = login_domain
        self.arn = resnodeaction.Add_Res_Node(dr)
        self.srmpg = sys_regionMgrPage.SysRegionMgrPage(dr)
        p_data = datainfo.get_xls_to_dict(
            "res_node_data.xlsx",
            "vmwareapi")["创建service-vmware"]
        self.arn.delete_service(
            p_data["regionname"],
            p_data["nodename"],
            p_data["servicename"])
        # 校验
        self.srmpg.open_sys_regionMgr_page()
        dr.wait(5)
        add_image(dr,"删除VMware服务")
        flag = dr.element_exist(
            "xpath->(//a[contains(text(),'%s')])" %
            p_data["servicename"])
        assert flag is False

    @allure.story("删除openstack服务")
    @pytest.mark.flaky(reruns=3)
    def test_delete_service_openstack(self,login_domain):
        dr = login_domain
        self.arn = resnodeaction.Add_Res_Node(dr)
        self.srmpg = sys_regionMgrPage.SysRegionMgrPage(dr)
        p_data = datainfo.get_xls_to_dict(
            "res_node_data.xlsx", "openstackapi")["创建service-keystone"]
        self.arn.delete_service(
            p_data["regionname"],
            p_data["nodename"],
            p_data["servicename"])
        self.srmpg.open_sys_regionMgr_page()
        dr.wait(5)
        add_image(dr,"删除openstack服务")
        flag = dr.element_exist(
            "xpath->(//a[contains(text(),'%s')])" %
            p_data["servicename"])
        assert flag is False
if __name__ == "__main__":
    pytest.main(["-s", "test_18_delete_service.py"])
