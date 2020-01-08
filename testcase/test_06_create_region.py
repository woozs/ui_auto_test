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

from public.common.publicfunction import *
from public.common import datainfo
from public.appmodel import resnodeaction
from public.pages import sys_regionMgrPage


@allure.feature("资源节点管理")
class TestCreateRegion():
    """测试添加资源节点"""

    @allure.story("创建资源节点")
    @pytest.mark.flaky(reruns=3)
    def test_create_region(self,login_domain):
        dr = login_domain
        p_data = datainfo.get_xls_to_dict("res_node_data.xlsx", "region")["创建资源节点"]
        arn = resnodeaction.Add_Res_Node(dr)
        srmpg = sys_regionMgrPage.SysRegionMgrPage(dr)
        arn.add_res_node(
            p_data["regionname"],
            p_data["nodename"],
            business_type=p_data["business_type"],
            platform=p_data["platform"],
            virtual_type=p_data["virtual_type"],
            regDesc=p_data["regDesc"])

        srmpg.open_sys_regionMgr_page()
        time.sleep(1)
        dr.wait(5)
        add_image(dr,"创建资源节点")
        flag = dr.element_exist(
            "xpath->//a[contains(text(),'%s')]" %
            p_data["nodename"])
        assert flag, "未查询到资源节点%s" % p_data["nodename"]


if __name__ == "__main__":
    pytest.main(["-s", "test_06_create_region.py"])
