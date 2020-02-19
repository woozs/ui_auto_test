# -*- coding: utf-8 -*-
# @Time    : 2020/2/10 14:42
# @Author  : mrwuzs
# @Email   : mrwuzs@outlook.com
# @File    : prodcategpage.py
# @Software: PyCharm

import allure
from public.pages import basepage
from config import globalparam



class FolderPgae(basepage.Page):
    pass

class ProdCateg(FolderPgae):
    """产品分类"""

    @allure.step("服务目录-产品分类页面")
    def open_prod_catg_page(self):
        self.log.debug("打开服务目录-产品分类页面")
        self.dr.open(globalparam.url + "/csdp/manage/#/manage-view/adminManage/folder/prodCateg")

    @allure.step("点击新建按钮")
    def click_new_create_button(self):
        self.log.debug("点击新建按钮")
        self.dr.click("xpath=//button[contains(.,'新建')]")

    #新建产品分类
    @allure.step("")
    def input_systematic_name(self,value):
        self.log.debug("输入分类名称")
        self.dr.type_and_enter("xpath=//input[@name='name']",value)

    def input_systematic_number(self,value):
        self.log.debug("输入分类序号")
        self.dr.type_and_enter("xpath=//input[@name='id']",value)

    def click_produc_category_icon(self):
        self.log.debug("点击产品分类图标")
        self.dr.click("xpath=//button[contains(.,'选择产品分类图标')]")

    def click_cloud_host(self):
        self.log.debug("点击云主机图标")
        self.dr.click("xpath=//li[contains(.,'云主机')]")

    def click_cloud_disk(self):
        self.log.debug("点击云磁盘图标")
        self.dr.click("xpath=//li[contains(.,'云磁盘')]")

    def click_bare_metal_server_icon(self):
        self.log.debug("点击裸金属服务器图标")
        self.dr.click("")

    def click_commit_button(self):
        self.log.debug("点击确认按钮")
        self.dr.click("xpath->//a[contains(.,'确定')]")

    def click_cancel_button(self):
        self.log.debug("点击取消按钮")
        self.dr.click("xpath->//a[contains(.,'取消')]")
    
    def input_describ(self,value):
        self.log.debug("输入描述")
        self.dr.type_and_enter("xpath=//div[5]/div/textarea",value)

    def click_submit_button(self):
        self.log.debug("点击保存按钮")
        self.dr.click("xpath=//button[@type='submit']")

    def click_create_page_cancel_button(self):
        self.log.debug("点击取消按钮")
        self.dr.click("xpath->//a[contains(.,'取消')]")




class ProductManagePage(FolderPgae):
    @allure.step("打开产品管理页面")
    def open_product_manage_page(self):
        pass

    
#操作系统管理
class  OperationSystemPage(FolderPgae):
    @allure.step("打开：服务目录-操作系统管理")
    def open_operation_sys_page(self):
        self.log.debug("打开操作系统管理页面")
        self.dr.open(globalparam.url+ "/csdp/manage/#/manage-view/adminManage/folder/operationsystem")

    @allure.step("点击新建按钮")
    def click_new_create_button(self):
        self.log.debug("点击新建按钮")
        self.dr.click("xpath=//button[contains(.,'新建')]")
    #
    # @allure.step("")