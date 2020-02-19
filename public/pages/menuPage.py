#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/23 15:37
# @Author  : mrwuzsmn,
# @Site    :
# @File    : menuPage.py
# @Software: PyCharm

from public.pages import basepage


class MenuPage(basepage.Page):

    def mova_to_menu_bar(self):
        self.dr.move_to_element("xpath -> //i")

    def click_res_node_mag(self):
        self.dr.click("xpath -> //li[contains(.,'资源节点管理')]")


    def move_to_project_view_button(self):
        self.log.debug("")
        self.dr.move_to_element("xpath=//li[contains(.,'项目视图')]")


