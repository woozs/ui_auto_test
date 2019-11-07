#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/24 8:43
# @Author  : mrwuzs
# @Site    : 
# @File    : dataCenterPage.py
# @Software: PyCharm
from public.common import basepage
from config import globalparam

class DataCenterPage(basepage.Page):

    def open_date_center_page(self):
        self.dr.open(globalparam.url+"/csdp/manage/#/manage-view/resource/sys_dataCenter")

    def click_selcet_mrg_button(self):
        self.dr.click("xpath->//div/div/div/div/div/div/span/span[2]/span")

    def input_select_mrg(self,value):
        self.dr.type_and_enter("xpath->(//input[@type='search'])[3]",value)

    def click_select_region(self):
        self.dr.click("xpath->//div[2]/div/div/span/span[2]/span")

    def input_select_region(self,value):
        self.dr.type_and_enter("xpath->(//input[@type='search'])[4]",value)

    #数据中心数
    def click_data_center(self,value):
        self.dr.click("xpath->//a[contains(text(),'%s')]"%value)

    #资源类型
    def click_select_res_type(self):
        self.dr.click("xpath->//div[3]/div/div/span/span[2]/span")

    def input_select_res_type(self,value):
        self.dr.clear_type("xpath->(//input[@type='search'])[5]",value)
    
    def click_commit_res_type(self):
        self.dr.click("xpath->//div[3]/span/span")

    #物理网络资源
    #物理网络
    def click_phy_net(self):
        self.dr.click("xpath->//a[contains(text(),'物理网络')]")

    #新建
    def click_create_phy_net_button(self):
        self.dr.click("xpath->(//button[@type='button'])[13]")

    #新建物理网络界面
    #网络类型
    def click_select_net_type(self):
        self.dr.click("xpath->//div[@id='net_modal']/form/div[2]/div/div/div/div/div/span/span[2]/span")

    def input_select_net_type(self,value):
        self.dr.type_and_enter("xpath->(//input[@type='search'])[8]",value)

    #流量类型
    def click_flow_type(self):
        self.dr.click("xpath->//div[@id='net_modal']/form/div[2]/div/div[2]/div/div/div/div/span")

    def input_flow_type(self,value):
        if self.dr.get_element("xpath->(//input[@type='search'])[9]").is_displayed():
            self.dr.get_element("xpath->(//input[@type='search'])[9]").click()
        self.dr.type_and_enter("xpath->(//input[@type='search'])[9]",value)

    #public
    def click_flow_type_public(self):
        self.dr.click("xpath->//div[3]/span/span")

    #guest
    def click_flow_type_guest(self):
        self.dr.click("xpath->//div[4]/span/span")
    #流量子类型
    def click_flow_sub_type(self):
        self.dr.click("xpath->//div[@id='net_modal']/form/div[2]/div/div[2]/div/div[2]/div/div/span")

    #dcn  cn2  internet zx
    def click_select_flow_sub_type(self,value):
        self.dr.click("xpath->//div[@id='net_modal']/form/div[2]/div/div[2]/div/div[2]/div/ul/li/div/span/span[text()='%s']"%value)
    
    def input_fow_sub_type(self,value):
        self.dr.type_and_enter("xpath->(//input[@type='search'])[10]",value)

    #vlan范围
    def input_start_vlan(self,value):
        self.dr.clear_type("xpath->//div[@id='net_modal']/form/div[2]/div/div[3]/div/div/input",value)

    def input_end_vlan(self,value):
        self.dr.clear_type("xpath->//div[@id='net_modal']/form/div[2]/div/div[3]/div/div[3]/input",value)

    #物理网络
    def input_phy_network(self,value):
        self.dr.clear_type("xpath->//div[@id='net_modal']/form/div[2]/div/div[4]/div/input",value)

    #交换机
    def input_switch(self,value):
        self.dr.clear_type("xpath->//div[@id='net_modal']/form/div[2]/div/div[5]/div/input",value)
    
    #保存
    def click_save_phy_net_button(self):
        self.dr.click("xpath->(//button[@type='submit'])[2]")

    #取消
    def click_cancel_phy_net_button(self):
        self.dr.click("xpath->//div[@id='net_modal']/form/div[3]/button[2]")

