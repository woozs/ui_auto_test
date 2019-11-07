#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/30 9:30
# @Author  : mrwuzs
# @Site    :
# @File    : test_15_delete_project.py
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
class TestProjectDelete(mytest.MyTest):
    """删除项目测试"""

    @allure.story("删除项目")
    @pytest.mark.flaky(reruns=3)
    def test_delete_project(self):

        login = Login(self.dr)
        datas = datainfo.get_xls_to_dict("user.xlsx", "Sheet1")[0]
        p_data = datainfo.get_xls_to_dict("projectdata.xlsx", "Sheet1")[0]

        ppg = authProjectPage.AuthProjectPage(self.dr)
        pac = projectAction.PojectAction(self.dr)
        # login.login("wuzs0001","1qaz!QAZ")
        login.login(datas["username"], datas["password"])
        # tenantname,projectname,projectdesc
        pac.delete_project(p_data["projectname"])
        ppg.open_authproject()
        ppg.input_and_search_project(p_data["projectname"])

        sleep(1)
        flag = self.dr.element_exist("xpath->//td")
        assert flag is False


if __name__ == "__main__":
    pytest.main(["-s", "test_15_delete_project.py"])
