#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/24 11:26
# @Author  : mrwuzs
# @Site    :
# @File    : vdcPage.py
# @Software: PyCharm

from public.pages import basepage
from config import globalparam


class VdcPage(basepage.Page):

    def open_vdc_page(self):
        self.dr.open(
            globalparam.url +
            "/csdp/manage/#/manage-view/adminManage/resVDCMgr")

    def click_new_vdc_buttun(self):
        self.log.debug("点击新建vdc按钮")
        self.dr.click("xpath->//div[3]/button")

    def input_vdc_name(self, value):
        self.log.debug("输入vdc名称")
        self.dr.clear_type("id->vdcName", value)

    def click_save_buttun(self):
        self.log.debug("点击保存按钮")
        self.dr.click("css->.modal-footer:nth-child(3) > .btn-warning")

    def search_vdc(self, value):
        self.log.debug("搜索vdc")
        self.dr.type_and_enter("xpath->(//input[@type='text'])[12]", value)

    def click_az_buttun(self):
        self.log.debug("点击可用区按钮")
        self.dr.click("css->.btn-link:nth-child(1)")

    def click_new_az_buttun(self):
        self.log.debug("点击新建可用区")
        self.dr.click("css->.mr-5")

    def input_az_name(self, value):
        self.log.debug("输入可用区名称")
        self.dr.clear_type("id->vPoolName", value)

    def click_resource_type(self):
        self.log.debug("点击资源类型")
        self.dr.click(
            "xpath->//*[@id='AddandEdit_form']/div/div[2]/div/div/div[1]/span/span[2]/span")

    def inpurt_resource_type(self, value):
        self.log.debug("输入资源类型")
        self.dr.type_and_enter("css->.open > .form-control", value)

    def click_type(self):
        self.log.debug("点击类型")
        self.dr.click(
            "xpath->//*[@id='AddandEdit_form']/div/div[5]/div/div/div[1]/span/span[2]/span")

    def input_type(self, value):
        self.log.debug("输入类型")
        self.dr.type_and_enter("css->.open > .form-control", value)

    def click_data_center(self):
        self.log.debug("点击数据中心")
        self.dr.click(
            "xpath->//*[@id='AddandEdit_form']/div/div[6]/div/div/div[1]/span/span[2]/span")

    def input_date_center(self, value):
        self.log.debug("输入数据中心")
        self.dr.type_and_enter("css->.ng-pristine > .form-control", value)

    def input_vPoolDesc(self, value):
        self.log.debug("输入可用区描述信息")
        self.dr.clear_type("id->vPoolDesc", value)

    def click_save_az_buttun(self):
        self.log.debug("点击保存按钮")
        self.dr.click("xpath->//*[@id='AddandEdit']/div[3]/button[1]")

    def search_vpool(self, value):
        self.log.debug("搜索可用区")
        self.dr.type_and_enter("xpath->(//input[@type='text'])[12]", value)

    def click_vpool_more_button(self):
        self.log.debug("点击更多按钮")
        self.dr.click("xpath->//td[10]/div/a")

    def click_delete_vpool_buttun(self):
        self.log.debug("点击删除vpool按钮")
        self.dr.click("xpath->(//button[@type='button'])[13]")

    def click_vpool_delete_btn_success(self):
        self.log.debug("点击确定按钮")
        self.dr.click("xpath->//a[contains(.,'确定')]")

    def click_vdc_delete_button(self):
        self.log.debug("点击删除按钮")
        self.dr.click("xpath->(//button[@type='button'])[14]")

    def click_vdc_more_button(self):
        self.log.debug("点击更多按钮")
        self.dr.click("xpath->//td[5]/div/a")

    def click_vdc_delete_btn_success(self):
        self.log.debug("点击确定按钮")
        self.dr.click("xpath->//a[contains(.,'确定')]")
