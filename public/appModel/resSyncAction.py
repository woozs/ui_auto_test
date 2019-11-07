#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/24 8:47
# @Author  : mrwuzs
# @Site    :
# @File    : resSyncAction.py
# @Software: PyCharm
import allure

from time import sleep
from public.pages import menuPage
from public.pages import resSyncPage
from public.common import log


class ResSync(object):
    def __init__(self, driver):
        self.dr = driver
        self.syncPage = resSyncPage.ResSyncPage(self.dr)
        self.log = log.Log()

    def phy_res_sync(self, reginname, datacenter, *args):
        """
        同步物理资源
        :param reginname:
        :param datacenter:
        :param args: 要同步的数据中心名称
        :return:
        """
        with allure.step("同步物理资源"):
            allure.attach("域：%s" % reginname)
            allure.attach("资源节点的名称:%s" % datacenter)
        self.log.info("同步物理资源")
        self.syncPage.open_ressyncpage()
        self.syncPage.open_osphysicalsyncpage()
        self.log.info("选择region：%s;" % reginname)
        sleep(1)
        self.syncPage.click_select_region()
        self.syncPage.select_region(reginname)
        self.log.info("选择数据中心:%s" % datacenter)
        self.syncPage.click_select_datacenter()
        self.syncPage.select_data_center(datacenter)
        for DC in args:
            with allure.step("选择数据中心"):
                allure.attach("数据中心名称:%s" % DC)
            self.syncPage.select_and_click_data_center(DC)
        self.syncPage.click_sync_buttun()
        sleep(1)
        # self.syncPage.switch_commit_page()
        self.syncPage.click_commit_buttun()


if __name__ == '__main__':
    from public.common import pyselenium
    from config import globalparam
    from public.appModel.loginAction import Login

    dr = pyselenium.PySelenium(globalparam.browser)
    dr.max_window()
    login = Login(dr).login("系统管理员", "123456")

    res = ResSync(dr)

    res.phy_res_sync("河南", "111111", "DC1", "DC2")
