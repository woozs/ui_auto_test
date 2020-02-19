#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/02/12 11:05
# @Author  : zn
# @Site    :
# @File    : test_22_create_product_classify.py
# @Software: PyCharm

import pytest
from public.common import datainfo
from public.pages import sysUorgMgrPage
from public.common.publicfunction import *
from public.appmodel import productaction

@allure.feature("服务目录管理")
class TestCreateProduct():
    """创建产品分类"""
    @allure.story("创建产品分分类")
#    @pytest.mark.flaky(reruns=3)
    def test_create_product(self,login_admin):
        dr = login_admin    #实现系统管理员登录
        dr.wait(10)
        datas = datainfo.get_xls_to_dict("product.xlsx", "Sheet1")["创建产品分类"]
        upage = sysUorgMgrPage.SysUorgMgrPage(dr)
        pa = productaction.ProductAction(dr)
        pa.create_productclassify(
            datas["cname"],
            datas["cnum"],
            datas["description"])
        # upage.input_select_user(datas["username"])
        # 查看用户，进行校验
        #upage.input_select_user(datas["username"])
        #add_image(dr, "创建用户")
        #assert dr.element_exist(
        #    "xpath->//span[contains(.,'%s')]" %
         #   datas["username"])



if __name__ == "__main__":
    pytest.main(["-s", "test_22_create_product_classify.py"])
