# -*- coding: utf-8 -*-
# @Time    : 2020/2/25 16:25
# @Author  : mrwuzs
# @Email   : mrwuzs@outlook.com
# @File    : test_13_product_manage.py
# @Software: PyCharm

import pytest

from public.common.publicfunction import *
from public.common import datainfo
from config import globalparam
from  public.appmodel import  folderaction
from config import globalparam


CASE_DATA =  datainfo.get_xls_to_dict("flolderdata.xlsx","产品管理")
@allure.feature("产品分类")
class TestProductMange():

    @allure.story("创建产品-云主机")
    @pytest.mark.flaky(reruns=globalparam.RENUM)
    @pytest.mark.dependency(depends=["test_create_prodcate_cloudhost"])
    def test_create_product_cloud_host(self,login_domain):
        self.dr = login_domain
        self.pra = folderaction.ProductManageAction(self.dr)
        data = CASE_DATA["创建产品-云主机"]
        time.sleep(globalparam.middle)
        self.pra.create_product(productclass=data["productclass"],
                                platform=data["platform"],
                                resourcetype=data["resourcetype"],
                                productname=data["productname"],
                                productbnum=data["productbnum"],
                                description=data["description"])
        time.sleep(globalparam.tiny)
        response = self.pra.search_product(productname=data["productname"])
        assert  data["productname"] in response
        assert data["productclass"] in response
        assert  data["productbnum"] in response


    @allure.story("创建产品-云磁盘")
    @pytest.mark.flaky(reruns=globalparam.RENUM)
    @pytest.mark.dependency(depends=["test_create_prodcate_cloudhost"])
    def test_create_product_cloud_disk(self,login_domain):
        self.dr = login_domain
        self.pra = folderaction.ProductManageAction(self.dr)
        data = CASE_DATA["创建产品-云磁盘"]
        time.sleep(globalparam.middle)
        self.pra.create_product(productclass=data["productclass"],
                                platform=data["platform"],
                                resourcetype=data["resourcetype"],
                                productname=data["productname"],
                                productbnum=data["productbnum"],
                                description=data["description"])
        time.sleep(globalparam.tiny)
        response = self.pra.search_product(productname=data["productname"])
        assert  data["productname"] in response
        assert data["productclass"] in response
        assert  data["productbnum"] in response


    @allure.story("产品上线-云主机")
    @pytest.mark.flaky(reruns=globalparam.RENUM)
    @pytest.mark.dependency(depends=["test_create_product_cloud_host"])
    def test_onine_product_cloud_host(self,login_domain):
        self.dr = login_domain
        self.pra = folderaction.ProductManageAction(self.dr)
        data = CASE_DATA["产品上线-云主机"]
        time.sleep(globalparam.middle)
        self.pra.product_online(productname=data["productname"])
        time.sleep(globalparam.tiny)
        response = self.pra.search_product(productname=data["productname"])
        assert "已上线"  in response

    @allure.story("产品上线-云磁盘")
    @pytest.mark.flaky(reruns=globalparam.RENUM)
    @pytest.mark.dependency(depends=["test_create_product_cloud_host"])
    def test_onine_product_cloud_disk(self,login_domain):
        self.dr = login_domain
        self.pra = folderaction.ProductManageAction(self.dr)
        data = CASE_DATA["产品上线-云磁盘"]
        time.sleep(globalparam.middle)
        self.pra.product_online(productname=data["productname"])
        time.sleep(globalparam.tiny)
        response = self.pra.search_product(productname=data["productname"])
        assert "已上线"  in response


if __name__ == "__main__":
    pytest.main(["-s", "test_13_product_manage.py"])
