#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/24 19:29
# @Author  : mrwuzs
# @Site    :
# @File    : authTenantPage.py
# @Software: PyCharm

from public.common import basepage
from config import globalparam


class AuthTenantPage(basepage.Page):

    def open_authtenant(self):
        self.dr.open(
            globalparam.url +
            "/csdp/manage/#/manage-view/adminManage/auth/tenant")

    def click_create_tenant_button(self):
        self.dr.click("xpath->//button[contains(.,'新建运营部门')]")

    def input_tenant_name(self, value):
        self.dr.clear_type("name->tenantName", value)

    def input_linkman_name(self, value):
        self.dr.clear_type("name->contact", value)

    def input_linkman_phoneno(self, value):
        self.dr.clear_type("name->phoneNo", value)

    def click_save_button(self):
        self.dr.click("xpath->//button[@type='submit']")

    def input_secrch_tenant(self, value):
        self.dr.type_and_enter(
            "xpath->//div[@class='col-md-3 padding-0']/form/div/div/input", value)

    def click_pull_down_button(self):
        self.dr.click("xpath->//div[@id='card']/div/div[2]/div/a[2]/i")

    def click_tenant_delete_button(self):
        self.dr.click("xpath->//a[contains(text(),'删除')]")

    def click_tenant_delete_success_button(self):
        self.dr.click("xpath->//a[contains(.,'确定')]")

    def click_tenant_view_details_button(self):
        self.dr.click("xpath->//a[contains(.,'查看详细')]")

    def click_post_button(self):
        self.dr.click("xpath->//a[contains(text(),'岗位')]")

    def click_user_num_button(self):
        self.dr.click("xpath->//td[3]/div/a")

    def click_remove_user_button(self):
        self.dr.click("xpath->//button[contains(.,'移除')]")

    def click_remove_user_success_button(self):
        self.dr.click("xpath->//a[contains(.,'确定')]")
