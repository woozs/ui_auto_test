# -*- coding: utf-8 -*-
# @Time    : 2020/2/25 21:33
# @Author  : mrwuzs
# @Email   : mrwuzs@outlook.com
# @File    : test_14_product_specification.py
# @Software: PyCharm


import pytest

from public.common.publicfunction import *
from public.common import datainfo
from config import globalparam
from  public.appmodel import  folderaction
from config import globalparam


CASE_DATA =  datainfo.get_xls_to_dict("flolderdata.xlsx","产品规格管理")
@allure.feature("产品分类")
class TestProductSp():
    @allure.story("创建产品规格-云主机")
    @pytest.mark.flaky(reruns=globalparam.RENUM)
    @pytest.mark.dependency()
    # @pytest.mark.dependency(depends=["test_create_product_cloud_host"])
    def test_create_product_sp_cloud_host(self,login_domain):
        self.dr = login_domain
        data = CASE_DATA["创建产品规格-云主机"]
        self.sp = folderaction.SpecificationAction(self.dr)
        self.sp.create_specification(productname=data["productname"],
                                     spname=data["spname"],
                                     sptype=data["sptype"],
                                     spdes=data["spdes"],
                                     vpool=data["vpool"]
                                     )
        response = self.sp.search_sp(spname=data["spname"])
        assert  data["spname"] in response
        assert data["productname"] in response

    @allure.story("创建产品规格-云磁盘")
    @pytest.mark.flaky(reruns=globalparam.RENUM)
    @pytest.mark.dependency()
    # @pytest.mark.dependency(depends=["test_create_product_cloud_disk"])
    def test_create_product_sp_cloud_disk(self,login_domain):
        self.dr = login_domain
        data = CASE_DATA["创建产品规格-云磁盘"]
        self.sp = folderaction.SpecificationAction(self.dr)
        self.sp.create_specification(productname=data["productname"],
                                     spname=data["spname"],
                                     sptype=data["sptype"],
                                     spdes=data["spdes"],
                                     vpool=data["vpool"]
                                     )
        response = self.sp.search_sp(spname=data["spname"])
        assert  data["spname"] in response
        assert data["productname"] in response

    @allure.story("产品规格上线-云主机")
    @pytest.mark.flaky(reruns=globalparam.RENUM)
    @pytest.mark.dependency(depends=["TestProductSp::test_create_product_sp_cloud_host"])
    def test_onine_product_cloud_host(self,login_domain):
        self.dr = login_domain
        self.sp = folderaction.SpecificationAction(self.dr)
        data = CASE_DATA["产品规格上线-云主机"]
        time.sleep(globalparam.middle)
        self.sp.online_sp( spname=data["spname"])
        time.sleep(globalparam.tiny)
        response = self.sp.search_sp(spname=data["spname"])
        assert "已上线"  in response

    @allure.story("产品规格上线-云磁盘")
    @pytest.mark.flaky(reruns=globalparam.RENUM)
    @pytest.mark.dependency(depends=["TestProductSp::test_create_product_sp_cloud_disk"])
    def test_onine_product_cloud_disk(self,login_domain):
        self.dr = login_domain
        self.sp = folderaction.SpecificationAction(self.dr)
        data = CASE_DATA["产品规格上线-云磁盘"]
        time.sleep(globalparam.middle)
        self.sp.online_sp( spname=data["spname"])
        time.sleep(globalparam.tiny)
        response = self.sp.search_sp(spname=data["spname"])
        assert "已上线"  in response



if __name__ == "__main__":
    pytest.main(["-s", "test_14_product_specification.py"])
