#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/25 10:07
# @Author  : mrwuzs
# @Site    : 
# @File    : projectAction.py
# @Software: PyCharm
import allure

from time import sleep
from public.pages import authProjectPage
from public.common import log

class PojectAction(object):
    def __init__(self, driver):
        self.dr = driver
        self.propg =authProjectPage.AuthProjectPage(self.dr)
        self.log = log.Log()

    def create_project(self,tenantname,projectname,projectdesc):
        with allure.step("创建项目"):
            allure.attach("运营部门名称：%s"%tenantname)
            allure.attach("项目名称：%s"%projectname)
            allure.attach("项目描述：%s"%projectdesc)
        self.propg.open_authproject()
        self.dr.wait(10)
        self.propg.click_new_create_buttun()
        sleep(1)
        self.propg.click_select_tenant()
        self.propg.input_and_select_tenant(tenantname)
        self.propg.click_select_zzjg()
        self.propg.select_zzjg(tenantname)
        self.propg.input_project_name(projectname)
        self.propg.input_project_desc(projectdesc)
        self.propg.click_save_new_project()

    def delete_project(self,projectname):
        with allure.step("删除项目"):
            allure.attach("项目名称：%s"%projectname)
        self.propg.open_authproject()
        self.dr.wait(10)
        self.propg.input_and_search_project(projectname)
        sleep(1)
        self.propg.click_project_more_button()
        sleep(0.5)
        self.propg.click_project_delete_button()
        sleep(0.5)
        self.propg.click_project_delete_success_button()


if __name__ == '__main__':
    from public.common import pyselenium
    from config import globalparam
    from public.appModel.loginAction import Login

    dr = pyselenium.PySelenium(globalparam.browser)
    dr.max_window()
    login = Login(dr).login("wuzs_auto_0001", "1qaz!QAZ")
    pa  = PojectAction(dr)
    # pa.create_project("wuzs_tenant_auto_001","wuzs_auto01_project","wuzs_auto")
    pa.delete_project("wuzs_auto01_project")