#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/30 11:47
# @Author  : mrwuzs
# @Site    :
# @File    : test_19_delete_region.py
# @Software: PyCharm

import time
import pytest
import allure

from public.common.publicfunction import *
from public.common import datainfo
from public.appmodel import resnodeaction
from public.pages import sys_regionMgrPage
from public.appmodel.loginaction import Login


@allure.feature("资源节点管理")
class TestDeleteRegion():
    """测试添加资源节点"""

    @allure.story("删除资源节点")
    @pytest.mark.flaky(reruns=3)
    def test_delete_region(self,login_domain):
        dr = login_domain
        p_data = datainfo.get_xls_to_dict("res_node_data.xlsx", "region")["创建资源节点"]
        arn = resnodeaction.Add_Res_Node(dr)
        srmpg = sys_regionMgrPage.SysRegionMgrPage(dr)
        arn.delete_res_node(p_data["regionname"], p_data["nodename"])
        # 搜索项目
        dr.wait(5)
        add_image(dr,"删除资源节点")
        srmpg.open_sys_regionMgr_page()
        flag = dr.element_exist(
            "xpath->//a[contains(text(),'%s')]" %
            p_data["nodename"])
        assert flag is False


if __name__ == "__main__":
    pytest.main(["-s", "test_19_delete_region.py"])
