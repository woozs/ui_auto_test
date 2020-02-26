#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/25 10:07
# @Author  : mrwuzs
# @Site    :
# @File    : projectaction.py
# @Software: PyCharm
import allure

from time import sleep
from public.pages import auth_project_page
from public.common import log
from  config import globalparam


class PojectAction(object):
    def __init__(self, driver):
        self.dr = driver
        self.propg = auth_project_page.AuthProjectPage(self.dr)
        self.log = log.Log()

    def create_project(self, tenantname, projectname, projectdesc):
        sleep(globalparam.small)
        with allure.step("创建项目"):
            allure.attach("运营部门名称：%s" % tenantname)
            allure.attach("项目名称：%s" % projectname)
            allure.attach("项目描述：%s" % projectdesc)
        self.propg.open_authproject()
        self.propg.click_new_create_buttun()
        sleep(globalparam.tiny)
        self.propg.click_select_tenant()
        self.propg.input_and_select_tenant(tenantname)
        self.propg.click_select_zzjg()
        self.propg.select_zzjg(tenantname)
        self.propg.input_project_name(projectname)
        self.propg.input_project_desc(projectdesc)
        self.propg.click_save_new_project()

    def delete_project(self, projectname):
        with allure.step("删除项目"):
            allure.attach("项目名称：%s" % projectname)
        self.propg.open_authproject()
        self.propg.input_and_search_project(projectname)
        sleep(globalparam.small)
        self.propg.click_project_more_button()
        sleep(globalparam.tiny)
        self.propg.click_project_delete_button()
        sleep(globalparam.tiny)
        self.propg.click_project_delete_success_button()

    def assign_admin_user_for_project(self,projectname,username):
        """
        给项目分配管理用户
        :param projectname:
        :param username:
        :return:
        """
        self.propg.open_authproject()
        self.propg.input_and_search_project(projectname)
        sleep(1)
        self.propg.click_project_name_button(projectname)
        self.propg.click_universal_role()
        self.propg.click_user_button()
        self.propg.click_select_user_button()
        sleep(1)
        self.propg.click_admin_user_button()
        self.propg.input_serach_user_box(username)
        sleep(1)
        self.propg.click_pitch_on_user()
        self.propg.click_common_confirm_button()


    def cancel_s_authorization(self,projectname,username):
        """
        用户的授权
        :param projectname:
        :param username:
        :return:
        """
        self.propg.open_authproject()
        self.propg.input_and_search_project(projectname)
        sleep(1)
        self.propg.click_project_name_button(projectname)
        self.propg.click_universal_role()
        self.propg.click_user_button()
        self.propg.click_serach_user_box_user_info(username)
        self.propg.click_common_remove_button()
        self.propg.click_common_confirm_button_tag_a()



if __name__ == '__main__':
    from public.common import pyselenium
    from config import globalparam
    from public.appmodel.loginaction import Login

    dr = pyselenium.PySelenium(globalparam.browser)
    dr.max_window()
    login = Login(dr).login("系统管理员", "123456")
    pa = PojectAction(dr)
    # pa.create_project("wuzs_tenant_auto_001","wuzs_auto01_project","wuzs_auto")
    # pa.assign_admin_user_for_project("湖北","hubei01")
    pa.cancel_s_authorization("湖北","hubei01")
    sleep(10)
    dr.quit()
