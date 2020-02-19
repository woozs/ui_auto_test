#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/25 17:58
# @Author  : mrwuzs
# @Site    :
# @File    : test_05_create_project.py
# @Software: PyCharm
import pytest

from public.common.publicfunction import *
from public.common import datainfo
from public.appmodel import projectaction
from public.pages import auth_project_page

@allure.feature("项目管理")
class TestProject():
    """测试创建项目"""

    @allure.story("创建项目")
    @pytest.mark.flaky(reruns=3)
    def test_create_project(self,login_admin):
        dr = login_admin
        p_data = datainfo.get_xls_to_dict("projectdata.xlsx", "Sheet1")["创建项目"]
        ppg = auth_project_page.AuthProjectPage(dr)
        pac = projectaction.PojectAction(dr)
        pac.create_project(
            p_data["tenantname"],
            p_data["projectname"],
            p_data["projectdesc"])
        ppg.open_authproject()
        ppg.input_and_search_project(p_data["projectname"])
        dr.wait(5)
        add_image(dr,"创建项目")
        text = dr.get_text(
            "xpath->//div[@class='box-body']/table-component/div/table/tbody")
        # 搜索项目
        assert p_data["projectname"] in text, "%s不在预期结果%s中" % (
            p_data["projectname"], text)
        assert p_data["tenantname"] in text, "%s不在预期结果%s中" % (
            p_data["tenantname"], text)


if __name__ == "__main__":
    pytest.main(["-s", "test_05_create_project.py"])
