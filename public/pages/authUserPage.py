#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/24 19:52
# @Author  : mrwuzs
# @Site    : 
# @File    : authUserPage.py
# @Software: PyCharm

from public.common import basepage
from config import globalparam

class AuthUsertPage(basepage.Page):


    def open_authuser(self):
        self.dr.open(globalparam.url+"/csdp/manage/#/manage-view/adminManage/auth/user")

    def click_crate_user_button(self):
        self.dr.click("xpath->(//button[@type='button'])[10]")

    def click_selcet_tenant(self):
        self.dr.click("xpath->//span/button/i")

    def input_select_tenant(self,value):
        self.dr.type_and_enter("xpath->//div[@id='selectClientModal']/div[2]/div/div/div/form/div/div/input",value)
        # self.dr.type_and_enter("xpath->//div[@id='selectClientModal']/div[@class='modal-body']/div/div[@class='row search-form-default']/"
        #                    "div[@class='col-md-12']/from/div[@class='input-group']/div[@class='input-count']/input"
        #                    ,value)

    def click_radio_tenant_name(self):
        self.dr.click("xpath->//div[@id='selectClientModal']/div[@class='modal-body']/div[@class='box-body form']/"
                      "table-component/div/table/tbody/tr/td[1]/div/span/input[@type='radio']")

    def click_commit_button(self):
        self.dr.click("xpath->//div[@id='selectClientModal']/div[@class='modal-footer']/"
                      "button[@class='btn btn-flat btn-primary']")

    def input_username(self,value):
        self.dr.clear_type("xpath->(//input[@name='username'])[2]",value)

    def input_firstname(self,value):
        self.dr.clear_type("xpath->(//input[@name='firstname'])[2]",value)

    def input_password(self,value):
        self.dr.clear_type("xpath->(//input[@name='password'])[2]",value)

    def input_repassword(self,value):
        self.dr.clear_type("xpath->(//input[@name='_repassword'])[2]",value)

    def input_email(self,value):
        self.dr.clear_type("xpath->(//input[@name='email'])[2]",value)

    def click_new_user_save_button(self):
        self.dr.click("xpath->//form/div[2]/div/div/button")

    def input_select_user(self, value):
        self.dr.type_and_enter("xpath->//div[@class='table-toolbar']/div/div//form/div/div/input", value)

    def click_user_more_button(self):
        self.dr.click("xpath->//span[contains(.,'更多')]")

    def click_user_delete_button(self):
        self.dr.click("xpath->//button[contains(.,'删除')]")

    def click_user_delete_success_button(self):
        self.dr.click("xpath->//a[contains(.,'确定')]")





