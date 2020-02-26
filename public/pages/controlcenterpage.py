# -*- coding: utf-8 -*-
# @Time    : 2020/2/19 15:36
# @Author  : mrwuzs
# @Email   : mrwuzs@outlook.com
# @File    : controlcenterpage.py
# @Software: PyCharm


import allure
from public.pages import basepage
from config import globalparam


class ControlCenterPage(basepage.Page):
    def click_entry_form_button(self):
        self.log.debug("单击加入申请单按钮")
        self.dr.click("xpath->//button[contains(.,'加入申请单')]")

    def click_confirmation_form_button(self):
        self.log.debug("单击取人申请单按钮")
        self.dr.click("xpath->//button[contains(.,'确认申请单')]")

class CloudHostPage(ControlCenterPage):

    def click_apply_cloudhost_button(self):
        self.log.debug("单击申请云主机按钮")
        self.dr.click("xpath->//button[contains(.,' 申请云主机')]")

    def click_box_vpool(self):
        self.log.debug("单击可用区下拉框")
        self.dr.click("xpath->//form[@id='serviceForm']/div/form-group-attr-component/div/div/div/div/span/span[2]/span")

    def input_and_search_box_vpool(self,value):
        self.log.debug("输入要选择的可用区")
        self.dr.type_and_enter("xpath->(//input[@type='search'])[3]",value)

    def click_ipv6_button(self):
        self.log.debug("单击IPV6按钮")
        self.dr.click("xpath->//button[contains(.,'6')]")

    def click_ipv4_button(self):
        self.log.debug("单击IPV4按钮")
        self.dr.click("xpath->//button[contains(.,'4')]")

    def click_subnet_box(self):
        self.log.debug("单击子网选择框")
        self.dr.click("xpath->//form-group-select-component/div/div/div/div/span/span[2]/span")

    def input_and_select_subnet(self,value):
        self.log.debug("输入要选择的子网，并按回车确定")
        self.dr.type_and_enter("xpath->(//input[@type='search'])[4]",value)

    def click_ip_box(self):
        self.log.debug("单击IP地址选择框")
        self.dr.click("xpath->//div[2]/div/div/div/input")

    def input_and_select_ip(self,value):
        self.log.debug("输入要选择的IP地址，并按回车确定")
        self.dr.type_and_enter("xpath->//div[2]/div/div/div/input",value)

    #目前只模板部署，后续添加
    def input_cpu(self,value):
        self.log.debug("输入CPU核数")
        self.dr.clear_type("xpath->//csdp-ui-slider/input",value)

    def input_mem(self,value):
        self.log.debug("输入内存，单位G")
        self.dr.clear_type("xpath->//form-group-attr-component[3]/div/div/csdp-ui-slider/input",value)

    def input_boot_disk(self,value):
        self.log.debug("输入系统盘大小，单位G")
        self.dr.clear_type("xpath->//form-group-attr-component[4]/div/div/csdp-ui-slider/input",value)

    def select_data_disk_button(self):
        self.log.debug("单击选择数据盘按钮")
        self.dr.click("xpath->//div[4]/div/div/button")

    def input_data_disk_size(self,value):
        self.log.debug("输入数据盘大小")
        self.dr.clear_type("xpath->//div/div/div/csdp-ui-slider/input",value)

    def input_cloud_host_name(self,value):
        self.log.debug("输入云主机名称")
        self.dr.clear_type("xpath->//input[@name='']",value)

    def click_add_host_num(self):
        self.log.debug("单击申请数量‘+’")
        self.dr.click("xpath->//form[@id='serviceForm']/div/form-group-number-component/div/div/div/a[2]/i")


class ShoppingcarPage(ControlCenterPage):
    """上项目视图申请单页面"""

    def click_submission_apply_form(self):
        self.log.debug("单击提交申请单")
        self.dr.click("xpath->//button[contains(.,'提交申请单')]")

    def commit_submit_button(self):
        self.log.debug("单击确认提交按钮")
        self.dr.click("xpath->//button[contains(.,'确认提交')]")

class ManageVolumePage(ControlCenterPage):
    def click_apply_volume_button(self):
        self.log.debug("单击申请云磁盘按钮")
        self.dr.click("xpath->//button[contains(.,' 申请云磁盘')]")

    def click_vpool_box(self):
        self.log.debug("单击可用去按钮")
        self.dr.click("xpath->//form[@id='serviceForm']/div/form-group-attr-component/div/div/div/div/span/span[2]/span")

    def  select_vpool(self,value):
        self.log.debug("选择可用去")
        self.dr.type_and_enter("xpath->//form-group-attr-component/div/div/div/input",value)

    def  input_volume_capacity(self,value):
        self.log.debug("输入云磁盘的容量")
        self.dr.clear_type("xpath->//csdp-ui-slider/input",value)

    def  click_independent_disk(self):
        self.log.debug("单击独立磁盘按钮")
        self.dr.click("xpath->//form-group-attr-component[3]/div/div/input")

    def input_volume_name(self,value):
        self.log.debug("输入云磁盘名称")
        self.dr.clear_type("xpath->//form-group-attr-component[3]/div/div/input",value)

    def click_number_application_add(self):
        self.log.debug("单击申请数量加按钮")
        self.dr.click("xpath->//form[@id='serviceForm']/div/form-group-number-component/div/div/div/a[2]")

    def click_cloud_host_category(self):
        self.log.debug("单击云主机类别")
        self.dr.click("xpath->//form-group-select-component/div/div/div/div/span/span[2]/span")

    def select_cloud_host_category(self,value):
        self.log.debug("选择云主机类别")
        self.dr.type_and_enter("xpath->//form-group-select-component/div/div/div/input",value)

    def select_cloud_host(self,value):
        self.log.debug("选择云主机")
        self.dr.click("xpath->//span[contains(.,'%s')]"%value)

    def select_volume(self,valume):
        self.log.debug("选择磁盘：%s"%valume)
        self.dr.type_and_enter("xpath->(//input[@type='text'])[10]",valume)

    def click_attach_button(self):
        self.log.debug("单击挂载按钮")
        self.dr.click("xpath->//td[8]/span/button")

    def  click_exclusive_button(self):
        self.log.debug("单击独享按钮")
        self.dr.click("xpath->(///input[@type='checkbox'])[4]")

    def click_share_button(self):
        self.log.debug("单击共享按钮")
        self.dr.click("xpath=(//input[@type='checkbox'])[5]")

    def click_host_for_attach_box(self):
        self.log.debug("单击云主机选择框")
        self.dr.click("xpath->//div[4]/div/div/div/div/div/span/span[2]/span")

    def select_host_for_attach(self,value):
        self.log.debug("选择要挂载的虚拟机")
        self.dr.type_and_enter("xpath->(//input[@type='search'])[6]",value)

    def click_commit_for_attach_buttton(self):
        self.log.debug("单击确定按钮")
        self.dr.click("xpath->//div[@id='attachVolumeModal']/div[3]/button")

    def click_volume_more_botton(self):
        self.log.debug("单击更多按钮")
        #这个按钮需要先把鼠标移动上去
        self.dr.move_to_element("xpath->//div/a/span")
        self.dr.click("xpath->//div/a/span")

    def click_release_button(self):
        self.log.debug("单击释放按钮")
        self.dr.click("xpath->//div/ul/li[2]/button")

    def click_release_commit_button(self):
        self.log.debug("单击确定按钮")
        self.dr.click("xpath->//a[contains(.,'确定')]")

#创建快照
    def click_create_snap_button(self):
        self.log.debug("单击创建磁盘快照按钮")
        self.dr.click("xpath->//button[contains(.,'创建快照')]")

    def  input_volume_sanp_name(self,value):
        self.log.debug("输入磁盘快照名称")
        self.dr.clear_type("xpath->//input[@name='snapshotName']",value)

    def  input_volume_snap_des(self,value):
        self.log.debug("输入磁盘快照的描述信息")
        self.dr.clear_type("xpath->(//textarea[@type='text'])[2]",value)

    def click_create_button_yellow(self):
        self.log.debug("点击创建按钮")
        self.dr.click("xpath->//div[@id='createVolumesnapshotModal']/form/div[2]/button")