#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/25 9:52
# @Author  : mrwuzs
# @Site    : 
# @File    : authProjectPage.py
# @Software: PyCharm
from public.common import basepage
from config import globalparam

class AuthProjectPage(basepage.Page):


    def open_authproject(self):
        self.dr.open(globalparam.url+"/csdp/manage/#/manage-view/adminManage/auth/projects")

    def click_new_create_buttun(self):
        self.dr.click("xpath->//div[5]/button/i")

    def click_select_tenant(self):
        self.dr.click("xpath->//span[contains(.,'请选择运营部门')]")

    def input_and_select_tenant(self,value):
        self.dr.type_and_enter("xpath->(//input[@type='search'])[3]",value)

    def click_select_zzjg(self):
        self.dr.click("xpath->//div[3]/div/div/button[2]/i")

    def input_project_name(self,value):
        self.dr.clear_type("name->projectName",value)

    def input_project_desc(self,value):
        self.dr.clear_type("name->projectDescription",value)

    def select_zzjg(self,value):
        self.dr.click("xpath->//a[contains(text(),'%s')]"%value)

    def click_save_new_project(self):
        self.dr.click("xpath->(//button[@type='button'])[10]")

    def input_and_search_project(self,value):
        self.dr.type_and_enter("xpath->//div[@class='table-toolbar']/div/div//form/div/div/input",value)

    def click_project_more_button(self):
        self.dr.click("xpath->//span[contains(.,'更多')]")

    def click_project_delete_button(self):
        self.dr.click("xpath->//button[contains(.,'删除')]")

    def click_project_delete_success_button(self):
        self.dr.click("xpath->//a[contains(.,'确定')]")