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
from public.common.publicfunction import *
from public.common import datainfo
from public.appmodel import projectaction
from public.pages import auth_project_page
from public.appmodel.loginaction import Login


@allure.feature("项目管理")
class TestProjectDelete():
    """删除项目测试"""

    @allure.story("删除项目")
    @pytest.mark.flaky(reruns=3)
    def test_delete_project(self,login_domain):
        dr = login_domain
        p_data = datainfo.get_xls_to_dict("projectdata.xlsx", "Sheet1")["创建项目"]
        ppg = auth_project_page.AuthProjectPage(dr)
        pac = projectaction.PojectAction(dr)
        pac.delete_project(p_data["projectname"])
        ppg.open_authproject()
        ppg.input_and_search_project(p_data["projectname"])
        sleep(1)
        dr.wait(5)
        add_image(dr,"删除项目")
        flag = dr.element_exist("xpath->//td")
        assert flag is False


if __name__ == "__main__":
    pytest.main(["-s", "test_15_delete_project.py"])
