#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/27 19:15
# @Author  : mrwuzs
# @Site    :
# @File    : test_07_create_service.py
# @Software: PyCharm

import pytest

from public.common.publicfunction import *
from public.common import datainfo
from public.appmodel import resnodeaction
from public.pages import sys_regionMgrPage


@allure.feature("资源节点管理")
class TestCreateService():
    """测试添加service"""

    @allure.story("创建VMware服务")
    @pytest.mark.flaky(reruns=3)
    def test_create_service_vmware(self,login_domain):
        dr = login_domain
        self.arn = resnodeaction.Add_Res_Node(dr)
        self.srmpg = sys_regionMgrPage.SysRegionMgrPage(dr)
        p_data = datainfo.get_xls_to_dict(
            "res_node_data.xlsx",
            "vmwareapi")["创建service-vmware"]
        self.arn.add_resource_service_node_vmware(
            p_data["regionname"],
            p_data["nodename"],
            p_data["servicename"],
            p_data["servicetype"],
            p_data["username"],
            p_data["passwrd"])
        # 校验
        dr.wait(5)
        add_image(dr,"创建VMware服务")
        self.srmpg.open_sys_regionMgr_page()

        flag = dr.element_exist(
            "xpath->(//a[contains(text(),'%s')])" %
            p_data["servicename"])
        assert flag

    @allure.story("创建opentack服务")
    @pytest.mark.flaky(reruns=3)
    def test_create_service_openstack(self,login_domain):
        dr = login_domain
        self.arn = resnodeaction.Add_Res_Node(dr)
        self.srmpg = sys_regionMgrPage.SysRegionMgrPage(dr)
        p_data = datainfo.get_xls_to_dict(
            "res_node_data.xlsx", "openstackapi")["创建service-keystone"]
        self.arn.add_resource_service_node_vmware(
            p_data["regionname"],
            p_data["nodename"],
            p_data["servicename"],
            p_data["servicetype"],
            p_data["username"],
            p_data["passwrd"])
        # 校验
        self.srmpg.open_sys_regionMgr_page()
        dr.wait(5)
        add_image(dr,"创建opentack服务")
        flag = dr.element_exist(
            "xpath->(//a[contains(text(),'%s')])" %
            p_data["servicename"])
        assert flag


if __name__ == "__main__":
    pytest.main(["-s", "test_07_create_service.py"])
