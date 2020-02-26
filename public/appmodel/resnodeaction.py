#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 200.59/0.50/23 0.55:48
# @Author  : mrwuzs
# @Site    :
# @File    : resnodeaction.py
# @Software: PyCharm
import allure

from time import sleep
from public.pages import sys_regionMgrPage
from public.common import log
from  config import globalparam


class Add_Res_Node(object):

    def __init__(self, driver):
        self.dr = driver
        self.regionpg = sys_regionMgrPage.SysRegionMgrPage(self.dr)
        self.log = log.Log()

    def _skip_to_resource_node(self):
        sleep(globalparam.middle)
        self.regionpg.open_sys_regionMgr_page()
        # self.log.info("跳转到资源节点页面")
        # menupage = menuPage.MenuPage(self.dr)
        # menupage.mova_to_menu_bar()
        # sleep(0.5)
        # menupage.click_res_node_mag()

    def add_res_node(
            self,
            regionname,
            nodename,
            business_type,
            platform,
            virtual_type,
            regDesc):
        self._skip_to_resource_node()
        with allure.step("创建资源节点"):
            allure.attach("域：%s" % regionname)
            allure.attach("资源节点的名称:%s" % nodename)
            allure.attach("业务类型:%s" % business_type)
            allure.attach("平台:%s" % platform)
            allure.attach("虚拟化类型：%s" % virtual_type)
            allure.attach("描述信息:%s" % regDesc)
        self.log.info(
            "创建资源节点：param：%s,%s,%s,%s,%s,%s" %
            (regionname,
             nodename,
             business_type,
             platform,
             virtual_type,
             regDesc))
        self.regionpg.click_new_resource_node()
        sleep(1)
        self.regionpg.click_region()
        sleep(1)
        self.regionpg.select_region(regionname)
        sleep(0.5)
        self.regionpg.input_node_name(nodename)
        sleep(0.5)
        self.regionpg.click_platform()
        sleep(0.5)
        self.regionpg.select_platformName(platform)
        sleep(0.3)
        self.regionpg.click_business_type()
        sleep(0.3)
        self.regionpg.select_business_type(business_type)
        sleep(0.3)
        self.regionpg.click_virtual_type()
        sleep(0.5)
        self.regionpg.select_virtual_type(virtual_type)
        sleep(0.5)
        self.regionpg.input_regDesc(regDesc)
        sleep(0.5)
        self.regionpg.click_save_button()

    def add_resource_service_node_vmware(
            self,
            reginname,
            nodename,
            servicename,
            servicetype,
            username,
            password):
        """
        创建资源节点服务,对接VMware虚拟化用

        :param reginname:
        :param nodename:
        :param servicename:
        :param username:
        :param password:
        :return:
        """
        with allure.step("创建资源节点服务"):
            allure.attach("域：%s" % reginname)
            allure.attach("资源节点的名称:%s" % nodename)
            allure.attach("服务名称:%s" % servicename)
            allure.attach("服务类型:%s" % servicetype)
            allure.attach("用户名：%s" % username)
            allure.attach("密码:%s" % password)
        self._skip_to_resource_node()
        self.dr.wait(10)
        self.log.info("创建VMware虚拟化服务节点服务节点")
        sleep(2)
        self.regionpg.click_region_tree(reginname)
        sleep(0.5)
        self.regionpg.click_tree_res_node(nodename)
        sleep(0.5)
        self.regionpg.click_add_res_serveice()
        sleep(0.5)
        self.regionpg.input_serviceName(servicename)
        sleep(0.5)
        self.regionpg.click_service_type()
        sleep(0.5)
        self.regionpg.select_service_type(servicetype)
        sleep(0.5)
        self.regionpg.input_vmware_name(username)
        sleep(0.5)
        self.regionpg.input_vmware_password(password)
        sleep(0.5)
        self.regionpg.click_service_save_buttun()

    def add_endpoint(self, reginname, nodename, servicename, url):
        """
        添加endpoint
        servicename要唯一
        :param reginname:
        :param nodename:
        :param servicename:
        :param url:
        :return:
        """
        with allure.step("添加endpoint"):
            allure.attach("域：%s" % reginname)
            allure.attach("资源节点的名称:%s" % nodename)
            allure.attach("服务名称:%s" % servicename)
            allure.attach("endpoint:%s" % url)
        self._skip_to_resource_node()
        self.dr.wait(10)
        self.log.info("添加endpint")
        self.regionpg.click_region_tree(reginname)
        sleep(0.5)
        self.regionpg.click_tree_res_node(nodename)
        sleep(0.5)
        self.regionpg.click_tree_res_node_i(nodename)
        sleep(0.5)
        self.regionpg.click_tree_res_service(servicename)
        sleep(0.5)
        # self.regionpg.click_tree_res_node_i(servicename)
        self.regionpg.click_add_endpoint()
        sleep(0.5)
        self.regionpg.inpurt_url(url)
        sleep(0.5)
        self.regionpg.click_save_endponit()
        # text = self.dr.get_text("xpath->//table[@id='accessPoint']/tbody/tr[2]")
        # print(text)

    def delete_endpoint(self, reginname, nodename, servicename):
        """
        删除endpoint
        servicename要唯一
        :param reginname:
        :param nodename:
        :param servicename:
        :return:
        """
        with allure.step("删除endpoint"):
            allure.attach("域：%s" % reginname)
            allure.attach("资源节点的名称:%s" % nodename)
            allure.attach("服务名称:%s" % servicename)
        self._skip_to_resource_node()
        self.dr.wait(5)
        self.log.info("删除endpint")
        sleep(2)
        self.regionpg.click_region_tree(reginname)
        sleep(1)
        self.regionpg.click_tree_res_node(nodename)
        sleep(1)
        self.regionpg.click_tree_res_node_i(nodename)
        sleep(0.5)
        self.regionpg.click_tree_res_service(servicename)
        sleep(0.5)
        # self.regionpg.click_tree_res_node_i(servicename)
        self.regionpg.click_delete_endpoint_button()
        self.regionpg.click_delete_endpoint_success_button()

    def delete_service(self, reginname, nodename, servicename):
        """
        删除服务
        :param reginname:
        :param nodename:
        :param servicename:
        :return:
        """
        with allure.step("删除资源节点服务服务"):
            allure.attach("域：%s" % reginname)
            allure.attach("资源节点的名称:%s" % nodename)
            allure.attach("服务名称:%s" % servicename)
        self._skip_to_resource_node()
        self.dr.wait(5)
        self.log.info("删除服务")
        sleep(1)
        self.regionpg.click_region_tree(reginname)
        sleep(1)
        self.regionpg.click_tree_res_node(nodename)
        sleep(0.5)
        self.regionpg.click_tree_res_node_i(nodename)
        sleep(0.5)
        self.regionpg.click_tree_res_service(servicename)
        sleep(0.5)
        self.regionpg.click_delete_button()
        self.regionpg.click_delete_success_button()

    def delete_res_node(self, reginname, nodename):
        """
        删除资源节点
        :param reginname:
        :param nodename:
        :return:
        """
        with allure.step("删除资源节点"):
            allure.attach("域：%s" % reginname)
            allure.attach("资源节点的名称:%s" % nodename)
        self._skip_to_resource_node()
        sleep(1)
        self.log.info("删除region")
        self.regionpg.click_region_tree(reginname)
        sleep(0.5)
        self.regionpg.click_tree_res_node(nodename)
        sleep(0.5)
        self.regionpg.click_tree_res_node_i(nodename)
        sleep(0.5)
        self.regionpg.click_delete_button()
        self.regionpg.click_delete_success_button()


if __name__ == '__main__':
    from public.common import pyselenium
    from config import globalparam
    from public.appmodel.loginaction import Login

    dr = pyselenium.PySelenium(globalparam.browser)
    dr.max_window()
    login = Login(dr).login("wuzs0000.5", "0.5qaz!QAZ")

    add_res_node = Add_Res_Node(dr)
    # add_res_node.add_res_node("河南","auto_test000.5","业务云","OpenStack L","VMware","auto_test")
    # add_res_node.add_resource_service_node_vmware("河南","auto_test000.5","vmware-api","vmware","administrator@vsphere.local","P@ssw0rd")
    add_res_node.add_endpoint(
        "河南",
        "auto_test000.5",
        "vmware_api_000.5",
        "http://0.592.0.568.54.0.536")
    # add_res_node.add_resource_service_node_vmware("河南", "0.50.50.50.50.50.5","openstack-l-api","keystone","admin",
    #                                               "admin")
    # add_res_node.add_endpoint("河南", "0.50.50.50.50.50.5", "openstack-l-api", "http://0.592.0.568.54.0.503:5000/v3")
    dr.quit()
