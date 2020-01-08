#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/24 15:04
# @Author  : mrwuzs
# @Site    :
# @File    : sysUorgMgrPage.py
# @Software: PyCharm

from public.pages import basepage
from config import globalparam


class SysUorgMgrPage(basepage.Page):

    def open_uorgmgrpage(self):
        self.dr.open(
            globalparam.url +
            "/csdp/manage/#/manage-view/systemManage/sys_uorgMgr")

    def click_new_user_buttun(self):
        self.dr.click("xpath->//div[3]/button")

    def click_select_mgr(self):
        self.dr.click(
            "xpath->/html/body/app-component/div[1]/main-component/div/div/manage-component/div/div/d"
            "iv/div[1]/div/div[2]/form/div[1]/div[1]/div/div/button[2]")

    def click_mgr(self, value):
        self.dr.click("xpath->//a[contains(text(),'%s')]" % value)

    def input_usrname(self, value):
        self.dr.clear_type("xpath->(//input[@name='username'])[2]", value)

    def input_first_password(self, value):
        self.dr.clear_type("xpath->(//input[@name='password'])[2]", value)

    def input_firstname(self, value):
        self.dr.clear_type("xpath->(//input[@name='firstname'])[2]", value)

    def input_repassword(self, value):
        self.dr.clear_type("xpath->(//input[@name='_repassword'])[2]", value)

    def input_email(self, value):
        self.dr.clear_type("xpath->(//input[@name='email'])[2]", value)

    def click_save_user_buttun(self):
        self.dr.click("xpath->//form/div[2]/div/div/button")

    def input_select_user(self, value):
        self.dr.type_and_enter(
            "xpath->//div[@class='table-toolbar']/div/div//form/div/div/input", value)

    def click_user_delete_button(self):
        self.dr.click("xpath->//button[contains(.,'删除')]")

    def click_user_more_button(self):
        self.dr.click("xpath->//span[contains(.,'更多')]")

    def click_user_delete_success_button(self):
        self.dr.click("xpath->//a[contains(.,'确定')]")
