# -*- coding: utf-8 -*-
# @Time    : 2020/2/12 15:39
# @Author  : mrwuzs
# @Email   : mrwuzs@outlook.com
# @File    : networkaction.py
# @Software: PyCharm

import allure

from time import sleep
from public.pages import  auth_project_page
from public.pages import networkpage
from public.common import log


class PojectNetwork(object):
    def __init__(self, driver):
        self.dr = driver
        self.netpage = networkpage.NetwoekPage(self.dr)
        self.projectpage =  auth_project_page.AuthProjectPage(self.dr)
        self.log = log.Log()


    def into_network_page(self,projectname):
        self.projectpage.open_authproject()
        self.projectpage.input_and_search_project(projectname)
        self.projectpage.click_project_network_button()
        

    def create_network(self,ipversion,networkname,vlan,gateway,netmask,tag,dhcp=True,vdc=None,vpool=None):
        self.netpage.click_new_create_button()
        if vdc:
            pass
        if vpool:
            pass
        if ipversion == "4":
            self.netpage.click_ipv4_button()
        elif  ipversion == "6":
            self.netpage.click_ipv6_button()
        else:
            self.log.error("ipversion ：%s is not found"%ipversion)

        self.netpage.click_vlan_input_box()
        self.netpage.input_text_new_create()
        self.netpage.input_network_name(networkname)
        self.netpage.input_vlan(vlan)
        self.netpage.input_gateway(gateway)
        self.netpage.input_netmask(netmask)
        self.netpage.inpute_tag(tag)
        if dhcp:
            self.netpage.click_enable_dhcp()
        self.netpage.click_save_button()

    def delete_network(self,networkname):
        pass

        # self.netpage.selet

    def create_subnet(self):
        pass

    def delete_subnet(self,subnetname):
        """
        根据子网名称删除子网
        :param subnetname:
        :return:
        """
        self.netpage.select_subnet(subnetname)
        self.netpage.click_delete_subnet_button()
        self.netpage.click_commit_delsubnet_button()


    def is_subnet_in_network(self,networkname):
        """
        判断该网络下是否存在子网
        :param networkname:
        :return: True/False
        """
        self.netpage.select_network(networkname)
        self.netpage.click_subnet_button()



if __name__ == '__main__':
    from public.common import pyselenium
    from config import globalparam
    from  public.appmodel.loginaction import Login
    dr = pyselenium.PySelenium(globalparam.browser)
    dr.max_window()
    login = Login(dr).login("hubei01", "1qaz!QAZ")
    import time
    time.sleep(2)
    dr.open("http://192.168.54.13/csdp/manage/#/manage-view/adminManage/auth/projects")
    net = PojectNetwork(dr)
    net.into_network_page("湖北")
    # net.create_network("4","test_netwrok_2014","2014","192.167.0.22","255.255.255.0","123")
    netpage = networkpage.NetwoekPage(dr)
    netpage.select_network("test_netwrok_2014")
    time.sleep(2)
    netpage.click_subnet_button()
    js = "document.getElementsByTagName('tbody')"
    dr.js(js)







    

