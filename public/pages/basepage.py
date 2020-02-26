#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/1 21:38
# @Author  : mrwuzs
# @Site    :
# @Software: PyCharm

from public.common import log
from config import globalparam
from public.common import publicfunction

class Page(object):
    """
    This is a base page class for Page Object.
    """

    def __init__(self, selenium_driver):
        self.dr = selenium_driver
        self.log = log.Log()



    def click_res_node_mag(self):
        self.log.debug("单击资源节点管理")
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
        self.log.debug("单击退出按钮")
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

    def mova_to_menu_bar(self):
        self.dr.move_to_element("xpath -> //div[@id='app']/section/header/div/div/div/span/button")


    def move_to_project_view_button(self):
        self.log.debug("")
        self.dr.move_to_element("xpath->//li[contains(.,'项目视图')]")


    def click_project_view_button(self):
        self.log.debug("单击项目视图按钮")
        self.dr.click("xpath->//li[contains(.,'项目视图')]")

    def move_to_project_cloud_host_button(self):
        self.log.debug("移动鼠标到云主机")
        self.dr.move_to_element("xpath->//span[contains(.,'云主机')]")

    def click_control_center_button(self):
        page = self.dr.origin_driver.page_source
        print(page)
        self.log.debug("单击控制中心-云主机按钮")
        self.dr.click("xpath->//span[text()='云主机快照']")
        # self.dr.js("arguments[0].click();", el)

    def click_cloud_host_snap_button(self):
        self.log.debug("单击云主机快照")
        self.dr.click("xpath->//span[contains(.,'云主机快照')]")

    def click_control_view(self):
        self.log.debug("鼠标单击概览按钮")
        self.dr.get_("xpath->//body/app-component")


    #项目视图
    def open_pv_cloudhost(self,projectname):
        self.log.debug("打开项目视图的控制中心云主机页面")
        prject_id = publicfunction.get_project_id(projectname)
        self.dr.open(globalparam.url+"/csdp/project/#/project/%s/control/manage_vm"%prject_id)

    def open_pv_managevolume_page(self,projectname):
        self.log.debug("打开项目视图的控制中心云磁盘页面")
        prject_id = publicfunction.get_project_id(projectname)
        self.dr.open(globalparam.url+"/csdp/project/#/project/%s/control/manage_volume"%prject_id)

    def open_shoppingcar_page(self,projectname):
        self.log.debug("打开申请单页面")
        prject_id = publicfunction.get_project_id(projectname)
        self.dr.open(globalparam.url+"/csdp/project/#/project/%s/shoppingcar"%prject_id)


    def page_to_bottom(self):
        self.log.debug("下滑页面到底部")
        self.dr.END()