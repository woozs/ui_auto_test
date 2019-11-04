#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/24 19:38
# @Author  : mrwuzs
# @Site    : 
# @File    : tenantAction.py
# @Software: PyCharm
import allure

from time import sleep
from public.pages import authTenantPage
from public.common import log

class TenantAction(object):
    def __init__(self, driver):
        self.dr = driver
        self.tenantpg =authTenantPage.AuthTenantPage(self.dr)
        self.log = log.Log()

    def create_tenant(self,tenantname,linkmanname,linkmanphoneno):
        """
        创建运营部门，由于时间原因，待改进，申请资源规划未处理，状态是否启用未处理，均采用默认
        :param tenantname:
        :param linkmanname:
        :param linkmanphoneno:
        :return:
        """
        with allure.step("创建运营部门"):
            allure.attach("运营部门名称：%s"%tenantname)
            allure.attach("联系人:%s"%linkmanname)
            allure.attach("联系电:%s"%linkmanphoneno)
        self.tenantpg.open_authtenant()
        sleep(1)
        self.tenantpg.click_create_tenant_button()
        self.tenantpg.input_tenant_name(tenantname)
        self.tenantpg.input_linkman_name(linkmanname)
        self.tenantpg.input_linkman_phoneno(linkmanphoneno)
        sleep(1)
        self.tenantpg.click_save_button()

    def delete_tenant(self,tenantname):
        with allure.step("删除运营部门"):
            allure.attach("运营部门名称：%s"%tenantname)
        self.tenantpg.open_authtenant()
        sleep(0.5)
        self.tenantpg.input_secrch_tenant(" ")
        self.tenantpg.input_secrch_tenant(tenantname)
        sleep(0.5)
        self.tenantpg.click_pull_down_button()
        sleep(0.5)
        self.tenantpg.click_tenant_delete_button()
        sleep(0.5)
        self.tenantpg.click_tenant_delete_success_button()

    def remove_post(self,tenantname):
        with allure.step("移除岗位"):
            allure.attach("运营部门名称：%s"%tenantname)
        self.tenantpg.open_authtenant()
        self.tenantpg.input_secrch_tenant(tenantname)
        sleep(0.5)
        self.tenantpg.click_tenant_view_details_button()
        sleep(0.5)
        self.tenantpg.click_post_button()
        sleep(0.5)
        self.tenantpg.click_user_num_button()
        sleep(0.5)
        self.tenantpg.click_remove_user_button()
        sleep(0.5)
        self.tenantpg.click_remove_user_success_button()




if __name__ == '__main__':
    from public.common import pyselenium
    from config import globalparam
    from public.appModel.loginAction import Login

    dr = pyselenium.PySelenium(globalparam.browser)
    dr.max_window()
    login = Login(dr).login("系统管理员", "123456")
    ta  = TenantAction(dr)
    # ta.create_tenant("wuzs_auto02","吴祖顺","13071089287")
    # ta.remove_post("wuzs_tenant_10236")
    ta.delete_tenant("wuzs_tenant_10236")