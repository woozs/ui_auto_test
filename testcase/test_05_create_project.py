#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/25 17:58
# @Author  : mrwuzs
# @Site    :
# @File    : test_05_create_project.py
# @Software: PyCharm
import pytest
import allure

from time import sleep
from public.common import mytest
from public.common import datainfo
from public.appModel import projectAction
from public.pages import authProjectPage
from public.appModel.loginAction import Login


@allure.feature("项目管理")
class TestProject(mytest.MyTest):
    """测试创建项目"""

    @allure.story("创建项目")
    @pytest.mark.flaky(reruns=3)
    def test_create_project(self):

        login = Login(self.dr)
        datas = datainfo.get_xls_to_dict("user.xlsx", "Sheet1")[0]
        p_data = datainfo.get_xls_to_dict("projectdata.xlsx", "Sheet1")[0]

        ppg = authProjectPage.AuthProjectPage(self.dr)
        pac = projectAction.PojectAction(self.dr)
        # login.login("wuzs0001","1qaz!QAZ")
        login.login(datas["username"], datas["password"])
        # tenantname,projectname,projectdesc
        pac.create_project(
            p_data["tenantname"],
            p_data["projectname"],
            p_data["projectdesc"])
        ppg.open_authproject()
        ppg.input_and_search_project(p_data["projectname"])
        text = self.dr.get_text(
            "xpath->//div[@class='box-body']/table-component/div/table/tbody")
        # 搜索项目
        assert p_data["projectname"] in text, "%s不在预期结果%s中" % (
            p_data["projectname"], text)
        assert p_data["tenantname"] in text, "%s不在预期结果%s中" % (
            p_data["tenantname"], text)


if __name__ == "__main__":
    pytest.main(["-s", "test_05_create_project.py"])
