#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/24 15:19
# @Author  : mrwuzs
# @Site    :
# @File    : useraction.py
# @Software: PyCharm
import allure

from time import sleep
from public.pages import authProductPage
from public.common import log


class ProductAction(object):
    def __init__(self, driver):
        self.dr = driver
        self.productpage = authProductPage.AuthProductPage(self.dr)
        self.log = log.Log()

    def create_productclassify(
            self,
            cname,
            cnum,
            description):
        with allure.step("创建产品分类"):
            allure.attach("分类名称：%s" % cname)
            allure.attach("描述:%s" % description)
        self.productpage.open_authProduct()
        sleep(2)
        self.productpage.click_crate_product_classify_button()
        self.productpage.input_clssifyname(cname)
        self.productpage.input_classifynum(cnum)
        self.productpage.click_select_classify_button()
        # self.productpage.click_select_classify_menu_button()
        self.productpage.click_assure_button()
        self.productpage.input_description(description)
        self.productpage.click_new_product_classify_save_button()




if __name__ == '__main__':
    from public.common import pyselenium
    from config import globalparam
    from public.appmodel.loginaction import Login

    dr = pyselenium.PySelenium(globalparam.browser)
    dr.max_window()
    login = Login(dr).login("系统管理员", "123456")
    #
    product = ProductAction(dr)
    sleep(2)
    product.create_productclassify("123","1","234")
    # # user.create_user("河南","wuzs0001","wuzs0001","1qaz!QAZ","1qaz!QAZ","wzs@qq.com")
    # user.create_tenant_user("wuzs_auto01", "wuzs_teant_0001", "wuzs_teant_0001", "1qaz!QAZ", "1qaz!QAZ", "wzs@qq.com")
    # user.allocation_domain_administrator("河南","wuzs0001")
    #
    sleep(5)
    dr.quit()