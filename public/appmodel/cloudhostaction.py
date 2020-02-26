# -*- coding: utf-8 -*-
# @Time    : 2020/2/19 15:33
# @Author  : mrwuzs
# @Email   : mrwuzs@outlook.com
# @File    : cloudhostaction.py
# @Software: PyCharm

import allure

from time import sleep
from public.pages import controlcenterpage
from public.common import log
from public.appmodel import applyfromaction


class CloudHostAction():
    def __init__(self, driver):
        self.dr = driver
        self.chpg = controlcenterpage.CloudHostPage(self.dr)
        self.cs = controlcenterpage.ShoppingcarPage(self.dr)
        self.log = log.Log()

    def into_pv_cloudhost(self,projectname):
        try:
            self.chpg.open_pv_cloudhost(projectname)
            # self.chpg.click_control_center_button()
        except  Exception as e:
            self.log.error("进入云主机模块失败：%s"%e)

    def create_cloud_host(self,hostname,**args):
        self.log.debug("创建虚拟机")
        try:
            self.chpg.click_apply_cloudhost_button()
            if "vpool" in args:
                self.chpg.click_box_vpool()
                self.chpg.input_and_search_box_vpool(args["vpool"])

            if  "ipversion" in args:
                self.log.debug("选择ip版本")
                if args["ipversion"] == "6":
                    self.chpg.click_ipv6_button()
                else:
                    self.chpg.click_ipv4_button()

            if "subnetname"  in args:
                self.log.debug("选择子网")
                self.chpg.click_subnet_box()
                self.chpg.input_and_select_subnet(args["subnetname"])

            if "ipaddress" in args:
                self.log.debug("选择IP地址")
                self.chpg.click_ip_box()
                self.chpg.input_and_select_ip(args["ipaddress"])

            if "cpu" in args:
                self.chpg.input_cpu(args["cpu"])

            if "mem" in args:
                self.chpg.input_mem(args["mem"])

            if "boot_disk"  in args:
                self.chpg.input_boot_disk(args["boot_disk"])

            if "data_disk" in args:
                self.chpg.select_data_disk_button()
                self.chpg.input_data_disk_size(args["data_disk"])
            self.chpg.input_cloud_host_name(hostname)

            if "host_num" in args:
                host_count = args["host_num"]
                while host_count -1 :
                    host_count  = host_count -1
                    self.chpg.click_add_host_num()
            self.chpg.click_entry_form_button()
            sleep(2)
            self.chpg.click_confirmation_form_button()
            self.cs.page_to_bottom()
            sleep(1)
            self.cs.click_submission_apply_form()

        except Exception as e:
            self.log.error("创建虚拟机失败：%s"%e)


if __name__ == '__main__':
    from public.common import pyselenium
    from config import globalparam
    from public.appmodel.loginaction import Login

    dr = pyselenium.PySelenium(globalparam.browser)
    dr.max_window()
    login = Login(dr).login("hubei01", "1qaz!QAZ")
    ch = CloudHostAction(dr)
    ch.into_pv_cloudhost("湖北")
    ch.create_cloud_host(hostname="bei02",vpool="湖北",cpu="4",mem="4",boot_disk="10",data_disk="200")
    sleep(6)
    dr.quit()



