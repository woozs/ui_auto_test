# -*- coding: utf-8 -*-
# @Time    : 2020/2/12 14:12
# @Author  : mrwuzs
# @Email   : mrwuzs@outlook.com
# @File    : networkpage.py
# @Software: PyCharm

import allure
from public.pages import basepage
from config import globalparam


class NetwoekPage(basepage.Page):

    def click_new_create_button(self):
        self.log.debug("单击新建网络按钮")
        self.dr.click("xpath->//button[contains(.,'新建')]")

    def click_ipv4_button(self):
        self.log.debug("单击ipv4按钮")
        self.dr.click("xpath->//button[contains(.,'4')]")

    def click_ipv6_button(self):
        self.log.debug("单击ipv6按钮")
        self.dr.click("xpath->//button[contains(.,'6')]")

    def input_network_name(self,value):
        self.log.debug("填写网络名称")
        self.dr.type("xpath->//input[@id='networkName']",value)

    def click_vlan_input_box(self):
        self.log.debug("单击vlan输入框")
        self.dr.click("xpath->//div[@id='addNet_modal']/div[2]/form/div/div[7]/div/div/div/span")

    def  input_text_new_create(self):
        self.log.debug("vlan选择选择新建")
        self.dr.type_and_enter("xpath->(//input[@type='search'])[7]","新建")


    def input_vlan(self,value):
        self.log.debug("输入vlan")
        self.dr.type("xpath->//input[@name='vlanId']",value)


    def input_gateway(self,value):
        self.log.debug("输入网关")

        # js = "$('[name=gateway]').val('%s')"%value
        #
        #由于无法触发IP地址，采取这种方式激活事件
        value1 = value+"1"
        js = "document.getElementsByName('gateway')[0].value = '%s'"%value1
        self.dr.js(js)
        self.dr.backspace("xpath->//input[@name='gateway']")


    def input_netmask(self,value):
        self.log.debug("输入子网掩码")
        js = "document.getElementsByName('netmask')[0].value = '%s'" % value
        self.dr.js(js)
        self.dr.click("xpath->//input[@name='netmask']")
        self.dr.type("xpath->//input[@name='netmask']","1")
        self.dr.backspace("xpath->//input[@name='netmask']")

    def inpute_tag(self,value):
        self.log.debug("输入网络标签")
        self.dr.type("xpath->(//input[@type='text'])[25]",value)

    def click_enable_dhcp(self):
        self.log.debug("单击开启dhcp")
        self.dr.click("xpath->//div[@id='addNet_modal']/div[2]/form/div/div[12]/div/div/span")

    def click_save_button(self):
        self.log.debug("单击保存按钮")
        self.dr.click("xpath->//div[@id='addNet_modal']/div[3]/button")

    def select_network(self,value):
        self.log.debug("查询网络-by-name")
        self.dr.type_and_enter("xpath->(//input[@type='text'])[12]",value)

    def click_subnet_button(self):
        self.log.debug("单击子网按钮")
        self.dr.click("xpath->//button[contains(.,'子网')]")

    #子网页面
    def select_subnet(self,value):
        self.log.debug("通过名称查询子网")
        self.dr.type_and_enter("xpath=(//input[@type='text'])[12]",value)

    # def
    def click_delete_subnet_button(self):
        self.log.debug("单击删除子网按钮")
        self.dr.click("xpath->//button[contains(.,' 删除')]")

    def click_commit_delsubnet_button(self):
        self.log.debug("单击删除确认按钮")
        self.dr.click("xpath->//a[contains(.,'确定')]")


