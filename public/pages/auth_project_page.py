#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/25 9:52
# @Author  : mrwuzs
# @Site    :
# @File    : auth_project_page.py
# @Software: PyCharm
from public.pages import basepage
from config import globalparam


class AuthProjectPage(basepage.Page):

    def open_authproject(self):
        self.log.debug("打开项目管理页面")
        self.dr.open(
            globalparam.url +
            "/csdp/manage/#/manage-view/adminManage/auth/projects")

    def click_new_create_buttun(self):
        self.log.debug("点击创建项目按钮")
        self.dr.click("xpath->//div[5]/button/i")

    def click_select_tenant(self):
        self.log.debug("点击选择运营部门")
        self.dr.click("xpath->//span[contains(.,'请选择运营部门')]")

    def input_and_select_tenant(self, value):
        self.log.debug("选择运营部门")
        self.dr.type_and_enter("xpath->(//input[@type='search'])[3]", value)

    def click_select_zzjg(self):
        self.log.debug("点击选择组织机构按钮")
        self.dr.click("xpath->//div[3]/div/div/button[2]/i")

    def input_project_name(self, value):
        self.log.debug("输入项目名称")
        self.dr.clear_type("name->projectName", value)

    def input_project_desc(self, value):
        self.log.debug("输入项目描述")
        self.dr.clear_type("name->projectDescription", value)

    def select_zzjg(self, value):
        self.log.debug("选择组织机构")
        self.dr.click("xpath->//a[contains(text(),'%s')]" % value)

    def click_save_new_project(self):
        self.log.debug("点击保存项目按钮")
        self.dr.click("xpath->(//button[@type='button'])[10]")

    def input_and_search_project(self, value):
        self.log.debug("搜索项目名称")
        self.dr.type_and_enter(
            "xpath->//div/div/div/div/div/div/div/div/form/div/div/input", value)

    def click_project_more_button(self):
        self.log.debug("点击更多按钮")
        self.dr.click("xpath->//span[contains(.,'更多')]")

    def click_project_delete_button(self):
        self.log.debug("点击删除按钮")
        self.dr.click("xpath->//button[contains(.,'删除')]")

    def click_project_delete_success_button(self):
        self.log.debug("点击确定按钮")
        self.dr.click("xpath->//a[contains(.,'确定')]")

    def click_project_network_button(self):
        self.log.debug("点击网络按钮")
        self.dr.click("xpath->//button[contains(.,'网络')]")

    def click_project_name_button(self,value):
        self.log.debug("单击项目名称按钮")
        self.dr.click("xpath->//td[contains(.,'%s')]/div/a"%value)

    def click_universal_role(self):
        self.log.debug("单击通用角色按钮")
        self.dr.click("xpath->//a[contains(text(),'通用角色（1）')]")

    def click_user_button(self):
        self.log.debug("单击用户按钮")
        self.dr.click("xpath->//button[contains(.,'用户')]")

    def click_select_user_button(self):
        self.log.debug("单击选择用户按钮")
        self.dr.click("xpath->//button[contains(.,'选择用户')]")

    #添加用户
    def click_admin_user_button(self):
        self.log.debug("单击管理用户")
        self.dr.click("xpath->//a[contains(text(),'管理用户')]")

    def input_serach_user_box(self,value):
        """点击选择用户后的页面"""
        self.log.debug("查询用户：%s"%value)
        self.dr.type_and_enter("xpath->(//input[@type='search'])[7]",value)

    def click_pitch_on_user(self):
        self.log.debug("选中用户")
        self.dr.click("xpath->//div[@id='addUserModal']/div[2]/div/form/table-component/div/table/thead/tr/th/div/span")


    #移除用户
    def click_serach_user_box_user_info(self,value):
        """角色 项目角色(通用) 的用户信息页面的输入框"""
        self.log.debug("查询用户：%s"%value)
        self.dr.type_and_enter("xpath->(//input[@type='search'])[4]",value)

    def click_remove_button(self):
        """操作下的移除按钮"""
        self.log.debug("点击移除按钮")
        self.dr.click("")