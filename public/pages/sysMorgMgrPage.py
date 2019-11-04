#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/24 16:03
# @Author  : mrwuzs
# @Site    : 
# @File    : sysMorgMgrPage.py
# @Software: PyCharm

from public.common import basepage
from config import globalparam


class SysMorgMgrPage(basepage.Page):

    def open_sys_morg_mgr_page(self):
        self.dr.open(globalparam.url+"/csdp/manage/#/manage-view/systemManage/sys_morgMgr")

    def select_mgr(self,value):
        self.dr.click("xpath->//a[contains(text(),'%s分公司')]"%value)

    def click_general_post(self):
        self.dr.click("xpath->//a[contains(text(),'通用岗位（1）')]")

    def click_user_buttun(self):
        self.dr.click("xpath->//button[contains(.,'用户')]")

    def click_seletc_user(self):
        self.dr.click("css->.yellow")

    def search_user(self,value):
        self.dr.type_and_enter("xpath->(//input[@type='search'])[5]",value)

    def click_search_user(self):
        self.dr.click("xpath->//div[@id='addUserModal']/div[2]/div/div/form/table-component/div/table/tbody/tr/td[1]/div/span/input[@type='radio']")

    def click_save_user(self):
        self.dr.click("xpath -> //div[@id='addUserModal']/div[@class='modal-footer']/button[@class='btn btn-warning']")

    def input_and_search_user(self,value):
        self.dr.type_and_enter("xpath->(//input[@type='search'])[4]",value)

    def click_remove_user_button(self):
        self.dr.click("xpath->//button[contains(.,'移除')]")

    def click_remove_user_success_button(self):
        self.dr.click("xpath->(//a[contains(@href, '#')])[2]")