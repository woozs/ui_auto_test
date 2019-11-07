#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/23 15:38
# @Author  : mrwuzs
# @Site    :
# @File    : sys_regionMgrPage.py
# @Software: PyCharm

from public.common import basepage
from config import globalparam


class SysRegionMgrPage(basepage.Page):

    def open_sys_regionMgr_page(self):
        self.dr.open(
            globalparam.url +
            "/csdp/manage/#/manage-view/systemManage/sys_regionMgr")

    def click_new_resource_node(self):
        self.dr.click("xpath->//button/i")

    def click_region(self):
        self.dr.click(
            "xpath -> //form[@id='regAddAndEdit_form']/div/div/div/div/div/span/span[2]/span ")

    def select_region(self, value):
        self.dr.type_and_enter("xpath -> (//input[@type='search'])[4]", value)

    def input_node_name(self, value):
        self.dr.clear_type("name -> regName_", value)

    def click_platform(self):
        self.dr.click("xpath -> //div[3]/div/div/div/span/span[2]/span")

    def select_platformName(self, value):
        self.dr.type_and_enter("xpath -> (//input[@type='search'])[5]", value)

    def input_regDesc(self, value):
        self.dr.clear_type("xpath ->//textarea[@name='regDesc'] ", value)

    def click_business_type(self):
        self.dr.click("xpath->//div[4]/div/div/div/span/span[2]/span")

    def select_business_type(self, value):
        self.dr.type_and_enter("xpath->(//input[@type='search'])[6]", value)

    def select_virtual_type(self, value):
        self.dr.type_and_enter("xpath->(//input[@type='search'])[7]", value)

    def click_virtual_type(self):
        self.dr.click("xpath->//div[2]/div[5]/div/div/div/span/span[2]")

    def click_save_button(self):
        self.dr.click("css->#regAddAndEdit .btn-primary")

    def click_clear_button(self):
        self.dr.click("xpath->//div[29]/div/div[3]/button[2]")

    def click_region_tree(self, value):
        self.dr.click(
            "xpath->//a[contains(.,'%s')]/parent::li//child::i" %
            value)

    def click_tree_res_node(self, value):
        self.dr.click("xpath->//a[contains(text(),'%s')]" % value)

    def click_add_res_serveice(self):
        self.dr.click("xpath -> //button[2]/i")

    def input_serviceName(self, value):
        self.dr.clear_type("name->serviceName", value)

    def click_service_type(self):
        self.dr.click("xpath->//div[2]/div/div/div/span/span[2]/span")

    def select_service_type(self, value):
        self.dr.type_and_enter("xpath->//div/div[2]/div/div/input", value)

    def input_vmware_name(self, value):
        self.dr.clear_type("name->authenInfo", value)

    def input_vmware_password(self, value):
        self.dr.clear_type("xpath->(//input[@name='authenInfo'])[2]", value)

    def click_service_save_buttun(self):
        self.dr.click("css->#serAddAndEdit .btn-primary")

    def click_tree_res_node_i(self, value):
        self.dr.click(
            "xpath->//a[contains(text(),'%s')]/parent::li//child::i" %
            value)

    def click_tree_res_service(self, value):
        self.dr.click("xpath->(//a[contains(text(),'%s')])" % value)

    def click_add_endpoint(self):
        self.dr.click("xpath->//i[contains(.,'添加')]")

    def inpurt_url(self, value):
        self.dr.clear_type("xpath->(//input[@type='text'])[13]", value)

    def click_save_endponit(self):
        self.dr.click("xpath->//td[4]/button")

    def click_commit_buttun(self):
        self.dr.click("xpath->//button[text()='确定']")

    def click_delete_endpoint_button(self):
        self.dr.click("xpath->//button[contains(.,'删除')]")

    def click_delete_endpoint_success_button(self):
        self.dr.click("xpath->//a[contains(.,'确定')]")

    def click_delete_button(self):
        self.dr.click("xpath->//button[6]/i")

    def click_delete_success_button(self):
        self.dr.click("xpath->//a[contains(.,'确定')]")
