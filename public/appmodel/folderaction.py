# -*- coding: utf-8 -*-
# @Time    : 2020/2/23 9:45
# @Author  : mrwuzs
# @Email   : mrwuzs@outlook.com
# @File    : folderaction.py
# @Software: PyCharm

import allure

from time import sleep
from public.pages import folderpage
from public.common import log
from config import  globalparam

class FolderAction(object):
    def __init__(self, driver):
        self.dr = driver
        self.log = log.Log()
        self.pdclasspage = folderpage.ProdCategPage(self.dr)
        self.pdmanagepage = folderpage.ProductManagePage(self.dr)
        self.spmanage = folderpage.SpecificationPage(self.dr)
        self.ospage = folderpage.OperationSystemPage(self.dr)


class ProdCategAction(FolderAction):

    def create_product_class(self,classname,classnum,classdes,prodclass):
        try:
            self.pdclasspage.open_prod_catg_page()
            sleep(1)
            self.pdclasspage.click_new_create_prod_button()
            self.pdclasspage.input_systematic_name(classname)
            self.pdclasspage.input_systematic_number(classnum)
            sleep(1)
            self.pdclasspage.click_produc_category_icon()
            sleep(2)
            if prodclass == "裸金属服务器":
                self.pdclasspage.click_bare_metal_server_icon()
            elif prodclass == "云主机":
                self.pdclasspage.click_cloud_host_icon()
            elif prodclass == "云磁盘":
                self.pdclasspage.click_cloud_disk_icon()
            elif prodclass == "物理资源":
                self.pdclasspage.click_phy_res_icon()
            elif prodclass =="负载均衡":
                self.pdclasspage.click_loadbalance_icon()
            elif prodclass == "公网IP":
                self.pdclasspage.click_public_ip_icon()
            elif prodclass == "云主机备份":
                self.pdclasspage.click_cloud_host_backup_icon()
            elif prodclass == "容器服务":
                self.pdclasspage.click_container_service_icon()
            elif prodclass == "外网带宽":
                self.pdclasspage.click_bandwidth_icon()
            else:
                self.log.error("产品分类:%s 不在可选列表中"%prodclass)
            self.pdclasspage.click_commit_button()
            self.pdclasspage.input_describ(classdes)
            self.pdclasspage.click_submit_button()
        except Exception as e:
            self.log.error("创建产品分类错误：%s"%e)

    def delete_product_class(self,classname):
        pass

    def search_product_class(self,classname):
        try:

            self.pdclasspage.open_prod_catg_page()
            self.pdclasspage.select_product_class(classname)
            data = self.pdclasspage.get_table_text()
            return  data
        except Exception as e:
            self.log.error("异常错误：%s"%e)
            return None


class ProductManageAction(FolderAction):
    def create_product(self,productclass,platform,resourcetype,productname,productbnum,description):
        try:
            self.pdmanagepage.open_product_manage_page()
            sleep(globalparam.middle)
            self.pdmanagepage.click_create_product_button()
            sleep(globalparam.tiny)
            self.pdmanagepage.click_product_class_box()
            self.pdmanagepage.select_product_class_name(productclass)
            self.pdmanagepage.click_platform_box()
            self.pdmanagepage.select_platform(platform)
            self.pdmanagepage.click_resource_type_box()
            self.pdmanagepage.select_resource_type(resourcetype)
            self.pdmanagepage.input_product_name(productname)
            self.pdmanagepage.input_product_num(productbnum)
            #目前都一样选择第一个
            self.pdmanagepage.click_get_url_button()
            sleep(globalparam.tiny)
            self.pdmanagepage.click_cloud_res_openup_button()
            self.pdmanagepage.page_to_bottom()
            sleep(globalparam.tiny)
            self.pdmanagepage.click_commit_button()
            self.pdmanagepage.input_product_des(description)
            sleep(globalparam.tiny)
            self.pdmanagepage.click_save_button()
            sleep(globalparam.tiny)
            self.pdmanagepage.click_save_button()

        except Exception as e:
            self.log.error("创建产品失败：%s"%e)


    def product_online(self,productname):
        try:
            self.pdmanagepage.open_product_manage_page()
            self.pdmanagepage.select_product(productname)
            self.pdmanagepage.click_more_button()
            sleep(globalparam.middle)
            self.pdmanagepage.click_online_button()
            self.pdmanagepage.click_common_confirm_button_tag_a()
        except Exception as e:
            self.log.error("异常错误：%s,产品上线失败"%e)

    def product_offline(self,productname):
        try:
            self.pdmanagepage.open_product_manage_page()
            self.pdmanagepage.select_product(productname)
            self.pdmanagepage.click_more_button()
            sleep(globalparam.tiny)
            self.pdmanagepage.click_offline_button()
            self.pdmanagepage.click_common_confirm_button_tag_a()
        except Exception as e:
            self.log.error("下线失败：%s"%e)

    def search_product(self,productname):
        try:
            self.pdmanagepage.open_product_manage_page()
            self.pdmanagepage.select_product(productname)
            data = self.pdclasspage.get_table_text()
            return data
        except Exception as e:
            self.log.error("查询失败：%s,异常错误")

class SpecificationAction(FolderAction):
    #sp简称规格
    def create_specification(self,productname,spname,sptype,spdes,vpool,**kwargs):
        try:
            self.spmanage.open_specification_page()
            self.spmanage.click_create_sp_button()
            sleep(globalparam.small)
            self.spmanage.select_product_name(productname)
            self.spmanage.input_spn_name(spname)
            if sptype == 2:
                self.spmanage.click_new_create_box()
            elif sptype == 1:
                self.spmanage.click_change_box()
            else:
                pass
            if "sptag" in kwargs:
                self.spmanage.input_sp_tag(kwargs["sptag"])

            self.spmanage.input_sp_des(spdes)
            self.spmanage.click_next_step_button()
            sleep(globalparam.middle)
            self.spmanage.page_to_bottom()
            self.spmanage.select_vpool(vpool)
            if "volume_type" in kwargs:
                self.spmanage.input_volume_type(kwargs["volume_type"])
            if "volume_disk_type_tag" in kwargs:
                self.spmanage.input_volume_disk_type_tag(kwargs["volume_disk_type_tag"])
            if "cloud_host_type"  in kwargs:
                self.spmanage.select_host_type(kwargs["cloud_host_type"])
            if "test_period" in kwargs:
                self.spmanage.select_test_period(kwargs["select_test_period"])
            self.spmanage.click_complete_button()
        except Exception as e:
            self.log.error("创建产品规格失败:%s"%e)


    def online_sp(self,spname):
        try:
            self.spmanage.open_specification_page()
            sleep(globalparam.small)
            self.spmanage.select_sp_name(spname)
            self.spmanage.click_more_button()
            sleep(globalparam.small)
            self.spmanage.click_online_button()
            self.spmanage.click_common_confirm_button_tag_a()
        except Exception as e:
            self.log.error("产品规格上线失败:%s"%e)

    def offline_sp(self,spname):
        try:
            self.spmanage.open_specification_page()
            sleep(globalparam.small)
            self.spmanage.select_sp_name(spname)
            self.spmanage.click_more_button()
            sleep(globalparam.small)
            self.spmanage.click_offline_button()
            self.spmanage.click_common_confirm_button_tag_a()
        except Exception as e:
            self.log.error("产品规格下线失败:%s"%e)

    def delete_sp(self,spname):
        try:
            self.spmanage.open_specification_page()
            sleep(globalparam.small)
            self.spmanage.select_sp_name(spname)
            self.spmanage.click_more_button()
            sleep(globalparam.small)
            self.spmanage.click_delete_sp_button()
            self.spmanage.click_common_confirm_button_tag_a()
        except Exception as e:
            self.log.error("产品规格上线失败:%s"%e)


    def search_sp(self,spname):
        try:
            self.spmanage.open_specification_page()
            sleep(globalparam.small)
            self.spmanage.select_sp_name(spname)
            sleep(globalparam.tiny)
            data = self.spmanage.get_table_text()
            return data
        except Exception as e:
            self.log.error("查询失败：%s,异常错误"%e)

class OSAction(FolderAction):
    def  create_os(self,vdc,vpool,imagetype,ostype,imagename):
        try:
            self.ospage.open_pv_managevolume_page()
            self.ospage.click_new_create_button()
            self.ospage.click_vdc_box()
            self.ospage.select_vdc(vdc)
            self.ospage.click_vpool_box()
            self.ospage.select_vpool(vpool)
            if imagetype == "模板":
                self.ospage.click_image_type_box()
                self.ospage.select_image_type("模板")
                self.ospage.click_os_type()
                self.ospage.select_os_type(ostype)
                self.ospage.click_template_box()
                self.ospage.select_template(imagename)
            elif imagetype == "ISO":
                self.ospage.click_image_type_box()
                self.ospage.select_image_type("ISO")
                self.ospage.click_os_type()
                self.ospage.select_os_type(ostype)
                self.ospage.click_iso_box()
                self.ospage.select_iso(imagename)
            elif imagetype == "自安装":
                self.ospage.click_image_type_box()
                self.ospage.select_image_type("ISO")
                self.ospage.click_os_type()
                self.ospage.select_os_type(ostype)
            else:
                self.log.error("imagetype is not in ‘模板’ iso 自安装")
            self.ospage.click_save_button()
        except  Exception as e:
            self.log.error("创建操作系统失败:%s"%e)

    def search_os(self):
        self.ospage.open_pv_managevolume_page()
        self



if __name__ == '__main__':
    from public.common import pyselenium
    from config import globalparam
    from public.appmodel.loginaction import Login

    dr = pyselenium.PySelenium(globalparam.browser)
    dr.max_window()
    login = Login(dr).login("hubei01", "1qaz!QAZ")
    #
    sleep(3)
    product =OSAction(dr)
    # # product.create_product("云主机","Openstack L","云主机","云主机测试","12","测试")
    # product.product_offline("云主机测试")
    # product.create_specification(productname="云主机",spname="云主机规格test",sptype=3,sptag="测试",spdes="自动化测试",vpool="湖北")
    print(product.create_os())
    sleep(2)
    # product.create_product_class("123","1","234")
    dr.quit()