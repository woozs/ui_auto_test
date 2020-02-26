#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/24 19:52
# @Author  : mrwuzs
# @Site    :
# @File    : authUserPage.py
# @Software: PyCharm

from public.pages import basepage
from config import globalparam
from time import sleep


class AuthProductPage(basepage.Page):

    def open_authProduct(self):
        self.log.debug("打开产品分类管理页面")
        self.dr.open(
            globalparam.url +
            "/csdp/manage/#/manage-view/adminManage/folder/prodCateg")

    def click_crate_product_classify_button(self):
        self.log.debug("单击创建产品分类按钮")
        self.dr.click("xpath->(//button[@type='button'])[10]")

    def input_clssifyname(self, value):
        self.log.debug("输入分类名称")
        self.dr.clear_type("xpath->//div/div/div[2]/div/input", value)

    def input_classifynum(self, value):
        self.log.debug("输入分类序号")
        self.dr.clear_type("xpath->/html/body/app-component/div[1]/main-component/div/div/manage-component/div/div/div/div/div[1]/div[1]/div[2]/form/div[1]/div/div[3]/div/input", value)

    def click_select_classify_button(self):
        self.log.debug("单击选择产品分类图标按钮")
        self.dr.click("xpath->/html/body/app-component/div[1]/main-component/div/div/manage-component/div/div/div/div/div[1]/div[1]/div[2]/form/div[1]/div/div[4]/div/div/span/button")

    def click_select_classify_menu_button(self, value):
        self.log.debug("选择产品分类图标")
        self.dr.click("xpath->/html/body/div[4]/div/div[2]/div/ul/li[2]/i")

    def click_assure_button(self):
        self.log.debug("单击确定按钮")
        self.dr.click("xpath->/html/body/div[4]/div/div[3]/div/button[1]")

    def input_description(self, value):
        self.log.debug("输入描述")
        self.dr.clear_type(
            "/html/body/app-component/div[1]/main-component/div/div/manage-component/div/div/div/div/div[1]/div[1]/div[2]/form/div[1]/div/div[5]/div/textarea",value)

    def click_new_product_classify_save_button(self):
        self.log.debug("单击保存按钮")
        self.dr.click("xpath->/html/body/app-component/div[1]/main-component/div/div/manage-component/div/div/div/div/div[1]/div[1]/div[2]/form/div[2]/div/div/button[1]")
