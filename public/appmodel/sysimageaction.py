# -*- coding: utf-8 -*-
# @Time    : 2020/2/27 10:26
# @Author  : mrwuzs
# @Email   : mrwuzs@outlook.com
# @File    : sysimageaction.py
# @Software: PyCharm

import allure
import time
from time import sleep

from public.pages import sysimagepage
from public.common import log


class ImageManageAction():
    def __init__(self, driver):
        self.dr = driver
        self.sip = sysimagepage.SysimagePage(self.dr)
        self.log = log.Log()

    def global_setting(self,provisiontype,networkadapter,diskcontrl=False,**kwargs):
        try:
            self.sip.open_sys_image()
            self.sip.click_global_setting()
            sleep(globalparam.middle)
            self.sip.click_edit_button()
            self.sip.click_preparation_type_box()
            self.sip.select_preparation_type(provisiontype)
            self.sip.click_network_adapter_type_box()
            self.sip.select_network_adapter_type(networkadapter)
            CLASS = self.sip.get_class_advanced_options_i_tag()
            if "fa-angle-up"  in CLASS:
                self.sip.click_advanced_options_button()
            elif "fa-angle-down"  in CLASS:
                self.log.debug("CLASS is ：%s nothing to do"%CLASS)
            else:
                self.log.error("CLASS:%s is error  please check ")
            if diskcontrl:
                self.sip.click_dc_os_box()
                self.sip.select_dc_os(kwargs["dcos"])
                self.sip.click_dc_os_version_box()
                self.sip.select_dc_os_version(kwargs["osverion"])
                if kwargs["controllertype"] == "IDE":
                    self.sip.click_dc_controllertype_box()
                    self.sip.select_dc_controllertype("IDE")
                if kwargs["controllertype"] == "SCSI":
                    self.sip.click_dc_controllertype_box()
                    self.sip.select_dc_controllertype("SCSI")
                    self.sip.click_dc_controller_box()
                    self.sip.select_dc_controller("controller")
            self.sip.click_save_button()
        except Exception as e:
            self.log.error("配置全局配置失败:%s"%e)

    
    def upload_file(self,imagename,path,timeout):
        try:
            self.sip.open_sys_image()
            sleep(globalparam.middle)
            self.sip.click_upload_button()
            sleep(globalparam.small)
            self.sip.input_image_name(imagename)
            self.sip.click_template_button()
            self.sip.click_vmdk_button()
            self.sip.upload_file_image(path)
            sleep(globalparam.tiny)
            self.sip.click_upload_button_for_childpage()
            sleep(timeout)
            t1 = time.time()
            response = self.sip.get_after_upload()
            while ("上传成功" not  in response) and (time.time() - t1 < timeout):
                response = self.sip.get_after_upload()
                sleep(1)
                self.log.debug("response:%s"%response)
            if "上传成功" not  in response:
                self.log.error("上次镜像失败或超时")
            self.sip.click_close_button()
            # self.sip.
        except  Exception as e:
            self.log.error(":%s"%e)

            
    def get_image_meg(self,imagename,regionname,resnode,dc):
        try:
            self.sip.open_sys_image()
            self.sip.select_image_name(imagename)
            self.sip.click_region_box()
            self.sip.select_region(regionname)
            self.sip.click_resnode_box()
            self.sip.select_resnode(resnode)
            self.sip.click_datacenter_box()
            self.sip.select_datacenter(dc)
            text = self.sip.get_text_iamge_table()
            return text
        except  Exception as e:
            self.log.error("异常错误：%s"%e)


if __name__ == '__main__':
    from public.common import pyselenium
    from config import globalparam
    from public.appmodel.loginaction import Login

    dr = pyselenium.PySelenium(globalparam.browser)
    dr.wait(10)
    dr.max_window()
    login = Login(dr).login("hubei01", "1qaz!QAZ")
    sleep(2)
    sys = ImageManageAction(dr)
    # sys.global_setting(provisiontype="厚置备置零",networkadapter="vmxnet2")
    path = r"E:\cmp\data\cirros-dianxin.vmdk"
    # sys.upload_file("test_04",path=path,timeout=10)
    text = sys.get_image_meg("test","湖北","湖北","DC1")
    print(text)

