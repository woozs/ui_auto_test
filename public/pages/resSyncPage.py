#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/24 9:06
# @Author  : mrwuzs
# @Site    :
# @File    : resSyncPage.py
# @Software: PyCharm


from public.pages import basepage
from config import globalparam


class ResSyncPage(basepage.Page):

    def open_ressyncpage(self):
        self.log.debug("打开资源同步页面")
        self.dr.open(
            globalparam.url +
            "/csdp/manage/#/manage-view/resource/sys_ResourceSynchroniz/osphysicalsync")

    def open_osphysicalsyncpage(self):
        self.log.debug("打开物理资源同步页面")
        self.dr.open(
            globalparam.url +
            "/csdp/manage/#/manage-view/resource/sys_ResourceSynchroniz/osphysicalsync")

    def click_phy_res_sync(self):
        self.log.debug("点击物理资源同步到云管")
        self.dr.click("xpath->//span[contains(.,'物理资源同步到云管')]")

    def click_select_region(self):
        self.log.debug("选择资源节点")
        self.dr.click("xpath->//div/div/div/div/div/div/span/span[2]/span")

    def click_select_datacenter(self):
        self.dr.click("xpath->//div[2]/div/div/span/span[2]/span")

    def select_region(self, value):
        self.dr.type_and_enter("xpath->(//input[@type='search'])[3]", value)

    def select_data_center(self, value):
        self.dr.type_and_enter("xpath->(//input[@type='search'])[4]", value)

    def select_and_click_data_center(self, value):
        self.dr.click(
            "xpath->//span[text()='%s']/parent::div/parent::td/parent::tr/child::td/child::div/child::span/child::input" %
            value)

    def click_sync_buttun(self):
        self.dr.click("xpath->//button[contains(.,' 同步')]")

    def click_commit_buttun(self):
        self.dr.click("xpath->//button[contains(.,'确定')]")
        # self.dr.click("css->.modal-footer:nth-child(3) > .btn-warning")

    def commit_buttun_element(self):
        self.dr.get_element("xpath->//button[contains(.,'确定')]")

    def is_exists_commit_buttun(self):
        self.log.debug("判断确定是否存在")
        return self.dr.element_exist("xpath->//button[contains(.,'确定')]")

    def switch_commit_page(self):
        self.dr.switch_to_frame("id->syncModal")

    def click_refresh_button(self):
        self.log.debug("点击刷新按钮")
        self.dr.click("xpath->//button[contains(.,' 刷新')]")

    def get_text_status(self, value):
        self.dr.get_text("xpath->//td[contains(.,'%s')]/../td[3]" % value)
