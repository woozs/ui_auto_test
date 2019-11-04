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

from public.common import mytest
from public.common import datainfo
from public.appModel import resNodeAction
from public.pages import sys_regionMgrPage
from public.appModel.loginAction import Login

@allure.feature("资源节点管理")
class TestDeleteRegion(mytest.MyTest):
    """测试添加资源节点"""

    @allure.story("删除资源节点")
    @pytest.mark.flaky(reruns=3)
    def test_delete_region(self):

        login = Login(self.dr)
        datas = datainfo.get_xls_to_dict("user.xlsx", "Sheet1")[0]
        p_data = datainfo.get_xls_to_dict("res_node_data.xlsx","region")[0]

        arn = resNodeAction.Add_Res_Node(self.dr)
        srmpg =sys_regionMgrPage.SysRegionMgrPage(self.dr)
        # login.login("wuzs0001","1qaz!QAZ")
        login.login(datas["username"],datas["password"])

        arn.delete_res_node(p_data["regionname"],p_data["nodename"])
        # text = self.dr.get_text("xpath->//div[@class='box-body']/table-component/div/table/tbody")
        #搜索项目


        srmpg.open_sys_regionMgr_page()
        flag = self.dr.element_exist("xpath->//a[contains(text(),'%s')]"%p_data["nodename"])
        assert flag is False


if __name__ == "__main__":
    pytest.main(["-s", "test_21_delete_user.py"])