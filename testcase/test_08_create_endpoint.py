#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/27 20:24
# @Author  : mrwuzs
# @Site    :
# @File    : test_08_create_endpoint.py
# @Software: PyCharm
import pytest
from public.common.publicfunction import *
from public.common import datainfo
from public.appmodel import resnodeaction
from public.pages import sys_regionMgrPage

@pytest.mark.usefixtures("driver")
@allure.feature("资源节点管理")
class TestCreateEndpoint():
    """测试添加Endpoint"""

    @allure.story("VMware创建endpoint")
    @pytest.mark.flaky(reruns=globalparam.RENUM)
    def test_vmware_endpoint(self,login_domain):
        """
        测试添加vmware，endpoint
        依赖已添加vmware服务
        :return:
        """
        dr = login_domain
        self.arn = resnodeaction.Add_Res_Node(dr)
        self.srmpg = sys_regionMgrPage.SysRegionMgrPage(dr)
        p_data = datainfo.get_xls_to_dict("res_node_data.xlsx", "endpoint")[
            "创建vmware-endpoint"]
        self.arn.add_endpoint(
            p_data["regionname"],
            p_data["nodename"],
            p_data["servicename"],
            p_data["url"])

        time.sleep(0.5)
        add_image(dr,"VMware创建endpoint")
        text = dr.get_text(
            "xpath->//table[@id='accessPoint']/tbody/tr[2]")
        assert p_data["url"] in text


    @allure.story("openstack创建endpoint")
    @pytest.mark.flaky(reruns=globalparam.RENUM)
    def test_openstack_endpoint(self,login_domain):
        """
        测试添加openstack，endpoint
        依赖已添加openstack服务
        :return:
        """
        dr = login_domain
        self.arn = resnodeaction.Add_Res_Node(dr)
        self.srmpg = sys_regionMgrPage.SysRegionMgrPage(dr)
        p_data = datainfo.get_xls_to_dict(
            "res_node_data.xlsx", "endpoint")["创建os-l-endpoint"]
        self.arn.add_endpoint(
            p_data["regionname"],
            p_data["nodename"],
            p_data["servicename"],
            p_data["url"])

        time.sleep(0.5)
        dr.wait(5)
        add_image(dr,"openstack创建endpoint")
        text = dr.get_text(
            "xpath->//table[@id='accessPoint']/tbody/tr[2]")
        assert p_data["url"] in text


if __name__ == "__main__":
    pytest.main(["-s", "test_08_create_endpoint.py"])
