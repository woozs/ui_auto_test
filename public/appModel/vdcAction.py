#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/24 11:34
# @Author  : mrwuzs
# @Site    : 
# @File    : vdcAction.py
# @Software: PyCharm
import allure
from time import sleep

from public.pages import vdcPage
from public.common import log

class VdcACction(object):
    def __init__(self, driver):
        self.dr = driver
        self.vdcpage =vdcPage.VdcPage(self.dr)
        self.log = log.Log()

    def ceate_vdc(self,vdcname):
        with allure.step("创建VDC"):
            allure.attach("VDC名称：%s" % vdcname)
        self.vdcpage.open_vdc_page()
        sleep(1)
        self.vdcpage.click_new_vdc_buttun()
        sleep(1)
        self.vdcpage.input_vdc_name(vdcname)
        self.vdcpage.click_save_buttun()

    def create_vpool(self,vdcname,vpool_name,resourcetype,typename,datacenter,vpooldesc):
        # typename_list =  ["数据中心","集群","主机"]
        #
        # if resourcetype != "虚拟资源" or resourcetype != "裸金属服务器":
        #     raise Exception("资源类型必须是数据中心或者裸金属服务器")
        # if typename not in typename_list:
        #     raise Exception("tyepename 必须是%s"%typename_list)
        with allure.step("创建vpool"):
            allure.attach("vdc：%s" % vdcname)
            allure.attach("vpool:%s"%vpool_name)
            allure.attach("资源类型:%s"%resourcetype)
            allure.attach("类型:%s"%typename)
            allure.attach("描述:%s"%vpool_name)
        self.vdcpage.open_vdc_page()
        sleep(0.5)
        self.vdcpage.search_vdc(vdcname)
        sleep(0.5)
        self.vdcpage.click_az_buttun()
        sleep(0.5)
        self.vdcpage.click_new_az_buttun()
        sleep(1)
        self.vdcpage.input_az_name(vpool_name)
        self.vdcpage.click_resource_type()
        self.vdcpage.inpurt_resource_type(resourcetype)

        self.vdcpage.click_type()
        self.vdcpage.input_type(typename)

        # self.vdcpage.click_data_center()
        # self.vdcpage.input_date_center(datacenter)

        self.vdcpage.input_vPoolDesc(vpooldesc)
        self.vdcpage.click_save_az_buttun()

    def delete_vpool(self,vdcname,vpoolname):
        with allure.step("删除vpool"):
            allure.attach("vdc：%s" % vdcname)
            allure.attach("vpool:%s"%vpoolname)
        self.vdcpage.open_vdc_page()
        sleep(0.5)
        self.vdcpage.search_vdc(vdcname)
        sleep(1)
        self.vdcpage.click_az_buttun()
        sleep(1)
        self.vdcpage.search_vpool(vpoolname)
        sleep(0.5)
        self.vdcpage.click_vpool_more_button()
        sleep(0.5)
        self.vdcpage.click_delete_vpool_buttun()
        sleep(1)
        self.vdcpage.click_vpool_delete_btn_success()

    def delete_vdc(self,vdcname):
        with allure.step("删除vdc"):
            allure.attach("vdc：%s" % vdcname)
        self.vdcpage.open_vdc_page()
        sleep(0.5)
        self.vdcpage.search_vdc(vdcname)
        sleep(0.5)
        self.vdcpage.click_vdc_more_button()
        sleep(0.5)
        self.vdcpage.click_vdc_delete_button()
        sleep(0.5)
        self.vdcpage.click_vpool_delete_btn_success()



if __name__ == '__main__':
    from public.common import pyselenium
    from config import globalparam
    from public.appModel.loginAction import Login

    dr = pyselenium.PySelenium(globalparam.browser)
    dr.max_window()
    login = Login(dr).login("wuzs_auto_0001", "1qaz!QAZ")

    vdc =VdcACction(dr)

    # vdc.delete_vpool("wuz_svdc_001","wzs_vpool_001")
    vdc.delete_vdc("wuz_svdc_001")
    sleep(5)

    dr.quit()

