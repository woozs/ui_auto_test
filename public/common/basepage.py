#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/1 21:38
# @Author  : mrwuzs
# @Site    :
# @Software: PyCharm
class Page(object):
    """
    This is a base page class for Page Object.
    """
    def __init__(self, selenium_driver):
        self.dr = selenium_driver

    def menu_bar_hovers(self):
        self.dr.get_element("xpath->//i")

    def click_res_node_mag(self):
        self.dr.click("xpath -> //li[contains(.,'资源节点管理')]")





