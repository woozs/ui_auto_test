#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/1 21:38
# @Author  : mrwuzs
# @Site    :
# @Software: PyCharm

from public.common import log
from config import globalparam

class Page(object):
    """
    This is a base page class for Page Object.
    """

    def __init__(self, selenium_driver):
        self.dr = selenium_driver
        self.log = log.Log()

    def menu_bar_hovers(self):
        self.log.debug("点击菜单按钮")
        self.dr.click("xpath->//i")

    def click_res_node_mag(self):
        self.log.debug("点击资源节点管理")
        self.dr.click("xpath -> //li[contains(.,'资源节点管理')]")

    def open_resource_overview(self):
        self.log.debug("打开项目管理页面")
        self.dr.open(
            globalparam.url +
            "/csdp/portal/#/resourceOverview")

    def open_project_view(self):
        self.log.debug("打开项目视图")
        self.dr.click()

    def move_to_el_icon_right(self):
        self.log.debug("鼠标悬停到下拉按钮")
        self.dr.move_to_element("xpath->//div[@id='app']/section/header/div/div/div[3]/div[3]/span/i")

    def click_logout_button(self):
        self.log.debug("点击退出按钮")
        self.dr.click("xpath->//ul/li[text()='退出']")

    def click_common_confirm_button(self):
        self.log.debug("单击确定按钮")
        self.dr.click("xpath->//button[contains(.,'确定')]")


    def click_common_remove_button(self):
        self.log.debug("单击移除按钮")
        self.dr.click("xpath->//button[contains(.,'移除')]")

    def click_common_confirm_button_tag_a(self):
        self.log.debug("单击确定按钮")
        self.dr.click("xpath->//a[contains(.,'确定')]")
