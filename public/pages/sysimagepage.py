# -*- coding: utf-8 -*-
# @Time    : 2020/2/11 15:36
# @Author  : mrwuzs
# @Email   : mrwuzs@outlook.com
# @File    : sysimagepage.py
# @Software: PyCharm

import allure
from public.pages import basepage
from config import globalparam

class SysimagePage(basepage.Page):
    def open_sys_image(self):
        self.log.debug("打开镜像管理页面")
        self.dr.open(globalparam.url + "/csdp/manage/#/manage-view/resource/sys_image")

    def select_image_name(self,value):
        self.log.debug("搜索镜像：%s"%value)
        self.dr.type_and_enter("xpath->(//input[@type='text'])[12]",value)

    def click_global_setting(self):
        self.log.debug("双击击全局配置")
        self.dr.move_to_element("xpath->//a[contains(text(),'全局配置')]")
        self.dr.double_click("xpath->//div[5]/div/a")

    def click_edit_button(self):
        self.log.debug("单击编辑按钮")
        self.dr.click("xpath->//div[@id='globalConfigModal']/form/div[2]/button")

    def click_preparation_type_box(self):
        self.log.debug("单击系统盘制备类型选择框")
        self.dr.click("xpath->//div[@id='editConfigModal']/form/div/div/div[2]/div/div/div/span/span[2]/span")

    def select_preparation_type(self,value):
        self.log.debug("选择置备类型")
        self.dr.type_and_enter("xpath->(//input[@type='search'])[8]",value)

    def click_network_adapter_type_box(self):
        self.log.debug("单击网络适配器选择框")
        self.dr.click("xpath->//div[@id='editConfigModal']/form/div/div/div[3]/div/div/div/span/span[2]/span")

    def select_network_adapter_type(self,value):
        self.log.debug("选择网络适配器选择框")
        self.dr.type_and_enter("xpath->(//input[@type='search'])[9]",value)

    def click_advanced_options_button(self):
        self.log.debug("单击高级选项")
        self.dr.click("xpath->//a[contains(text(),'高级选项')]")

    def get_class_advanced_options_i_tag(self):
        self.log.debug("获取高级选项后的箭头的属性")
        return self.dr.get_attribute("xpath->//div[4]/div/label/a/i","class")

    def click_dc_os_box(self):
        self.log.debug("单击磁盘控制器下的操作系统选择框")
        self.dr.click("xpath->//div[@id='ui-select-choices-row-18-0']/span/span")

    def click_dc_os_version_box(self):
        self.log.debug("单击磁盘控制器下的操作系统版本选择框")
        self.dr.click("xpath->//div[@id='editConfigModal']/form/div/div/div[6]/div[2]/div/div/span/span[2]/span")

    def click_dc_controllertype_box(self):
        self.log.debug("单击磁盘控制器下的控制器类型选择框")
        self.dr.click("xpath->//div[@id='editConfigModal']/form/div/div/div[6]/div[3]/div/div/span/span[2]/span")

    def click_dc_controller_box(self):
        self.log.debug("单击磁盘控制器下的控制器选择框")
        self.dr.click("xpath->//div[@id='editConfigModal']/form/div/div/div[6]/div[4]/div/div/span/span[2]/span")

    def select_dc_os(self,value):
        self.log.debug("选择操作系统")
        self.dr.type_and_enter("xpath->(//input[@type='search'])[10]",value)

    def select_dc_os_version(self,value):
        self.log.debug("选择操作系统版本")
        self.dr.type_and_enter("xpath->(//input[@type='search'])[11]",value)

    def select_dc_controllertype(self,value):
        """
        value in IDE,SCSI
        """
        self.log.debug("选择操作控制器类型")
        self.dr.type_and_enter("xpath->(//input[@type='search'])[12]",value)

    def select_dc_controller(self,value):
        """
        :param value: SI Logic 并行,LSI Logic SAS , VMware 准虚拟 ,BusLogic 并行
        :return:
        """
        self.log.debug("选择操作控制器")
        self.dr.type_and_enter("xpath->(//input[@type='search'])[14]",value)

    def click_add_button(self):
        self.log.debug("单击加号按钮")
        self.dr.click("xpath->//div[@id='editConfigModal']/form/div/div/div[6]/div[5]/button[2]/i")
    
    def click_save_button(self):
        self.log.debug("单击保存按钮")
        self.dr.click("xpath->//div[@id='editConfigModal']/form/div[2]/button")

#上次镜像
    def click_upload_button(self):
        self.log.debug("单击上传按钮")
        self.dr.click("xpath->//div[5]/div/button")

    def input_image_name(self,value):
        self.log.debug("输入镜像名称")
        self.dr.clear_type("xpath->//input[@name='mirrorName']",value)

    def click_template_button(self):
        self.log.debug("单击模板按钮")
        self.dr.click("xpath->//form[@id='fileuploadMirror']/div[2]/div/div[4]/div/button")

    def click_iso_button(self):
        self.log.debug("单击ISO按钮")
        self.dr.click("xpath->//form[@id='fileuploadMirror']/div[2]/div/div[4]/div/button[2]")

    def click_vmdk_button(self):
        self.log.debug("单击vmdk按钮")
        self.dr.click("xpath->//form[@id='fileuploadMirror']/div[2]/div/div[5]/div/button")

    def click_ova_button(self):
        self.log.debug("单击ova按钮")
        self.dr.click("xpath->//form[@id='fileuploadMirror']/div[2]/div/div[5]/div/button[2]")

    def click_ostype_box_upload(self):
        self.log.debug("点击操作系统类型选择框")
        self.dr.click("xpath->//form[@id='fileuploadMirror']/div[2]/div/div[6]/div/div/div/span/span[2]/span")
    
    def select_ostype_upload(self,value):
        self.log.debug("选择操作系系统类型")
        self.dr.type_and_enter("xpath->(//input[@type='search'])[10]",value)

    def click_osversion_box_upload(self):
        self.log.debug("点击操作系统版本选择框")
        self.dr.click("xpath->//form[@id='fileuploadMirror']/div[2]/div/div[6]/div[2]/div/div/span/span[2]/span")

    def select_osversion_upload(self,value):
        self.log.debug("选择操作系系统版本")
        self.dr.type_and_enter("xpath->(//input[@type='search'])[11]",value)

    def input_minimum_memory(self,value):
        self.log.debug("输入最小内存")
        self.dr.clear_type("xpath->//input[@name='minRam']",value)

    def input_minimum_disk(self,value):
        self.log.debug("输入最小磁盘")
        self.dr.clear_type("xpath->//input[@name='size']",value)

    def upload_file_image(self,vlaue):
        self.log.debug("单击上传文件按钮")
        ele = self.dr.get_element("xpath->//input[@name='inputFile']")
        ele.send_keys(vlaue)

    def click_upload_button_for_childpage(self):
        self.log.debug("单击上传按钮")
        self.dr.click("xpath->//form[@id='fileuploadMirror']/div[2]/div/div[9]/div/table/tbody/tr/td[5]/button/span")

    def get_after_upload(self):
        self.log.debug("获取上次后的结果")
        TEXT = self.dr.get_text("xpath->//form[@id='fileuploadMirror']/div[2]/div/div[9]/div/table/tbody/tr/td[2]")
        return  TEXT
    
    def click_close_button(self):
        self.log.debug("单击关闭按钮")
        self.dr.click("xpath->//form[@id='fileuploadMirror']/div[3]/button")
    
    def select_image_name_box(self,value):
        self.log.debug("搜索镜像")
        self.dr.type_and_enter("xpath->(//input[@type='text'])[12]",value)

    def click_region_box(self):
        self.log.debug("单击区域选择框")
        self.dr.click("xpath->//div[2]/div/div/span/span[2]/span")

    def click_resnode_box(self):
        self.log.debug("单击资源节点选择框")
        self.dr.click("xpath->//div[3]/div/div/span/span[2]/span")

    def click_datacenter_box(self):
        self.log.debug("单击数据中心选择框")
        self.dr.click("xpath->//div[4]/div/div/span/span[2]/span")

    def select_region(self,value):
        self.log.debug("选择区域")
        self.dr.type_and_enter("xpath->(//input[@type='search'])[3]",value)

    def select_resnode(self,value):
        self.log.debug("选择资源节点")
        self.dr.type_and_enter("xpath->(//input[@type='search'])[4]",value)

    def select_datacenter(self,value):
        self.log.debug("选择数据中心")
        self.dr.type_and_enter("xpath->(//input[@type='search'])[5]",value)

    def get_text_iamge_table(self):
        self.log.debug("获取镜像列表的文本信息")
        eles = self.dr.get_elements("xpath->//mirror-table/div/table/tbody/tr")
        texts = []
        for ele in eles:
            texts.append(ele.text)
            # texts.append(ele.text())
        return texts

