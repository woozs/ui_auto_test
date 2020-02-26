# -*- coding: utf-8 -*-
# @Time    : 2020/2/25 14:33
# @Author  : mrwuzs
# @Email   : mrwuzs@outlook.com
# @File    : test_12_prodcate.py
# @Software: PyCharm

import time
import pytest

from public.common.publicfunction import *
from public.common import datainfo
from config import globalparam
from  public.appmodel import  folderaction


CASE_DATA =  datainfo.get_xls_to_dict("flolderdata.xlsx","产品分类")

@allure.feature("产品分类")
class TestProdCate():
    """测试产品分类"""
    @allure.story("创建产品分类-云主机")
    @pytest.mark.flaky(reruns=globalparam.RENUM)
    def test_create_prodcate_cloudhost(self,login_domain):
        self.dr = login_domain
        self.pda =folderaction.ProdCategAction(self.dr)
        data = CASE_DATA["创建产品分类-云主机"]
        time.sleep(globalparam.middle)
        self.pda.create_product_class(classname=data["classname"],
                                      classnum=data["classnum"],
                                      classdes=data["classdes"],
                                      prodclass=data["prodclass"])
        time.sleep(globalparam.tiny)
        response =  self.pda.search_product_class(data["classname"])
        assert  data["classname"] in response
        assert  data["classdes"] in response

    @allure.story("创建产品分类-云磁盘")
    @pytest.mark.flaky(reruns=globalparam.RENUM)
    def test_create_prodcate_clouddisk(self,login_domain):
        self.dr = login_domain
        self.pda =folderaction.ProdCategAction(self.dr)
        data = CASE_DATA["创建产品分类-云磁盘"]
        time.sleep(globalparam.middle)
        self.pda.create_product_class(classname=data["classname"],
                                      classnum=data["classnum"],
                                      classdes=data["classdes"],
                                      prodclass=data["prodclass"])
        time.sleep(globalparam.tiny)
        response =  self.pda.search_product_class(data["classname"])
        assert  data["classname"] in response
        assert  data["classdes"] in response



if __name__ == "__main__":
    pytest.main(["-s", "test_12_prodcate.py"])
