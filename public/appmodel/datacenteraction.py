#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/6 16:15
# @Author  : mrwuzs
# @Site    :
# @File    : datacenteraction.py
# @Software: PyCharm

import allure
from public.pages import dataCenterPage
from public.common import log


class DataCenterAction(object):

    def __init__(self, driver):
        self.dr = driver
        self.dcPg = dataCenterPage.DataCenterPage(self.dr)
        self.log = log.Log()

    @allure.step("选择资源类型")
    def select_resouce_type(self, mrgname, regionname, resourcetype):
        """选择资源类型"""
        self.dcPg.open_date_center_page()
        self.dr.wait(5)
        self.dcPg.click_selcet_mrg_button()
        self.dcPg.input_select_mrg(mrgname)
        self.dcPg.click_select_region()
        self.dcPg.input_select_region(regionname)
        self.dcPg.click_select_res_type()
        self.dcPg.input_select_res_type(resourcetype)
        self.dcPg.click_commit_res_type()
