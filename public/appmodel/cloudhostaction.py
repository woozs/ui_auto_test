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


class CloudHostAction():
    def __init__(self, driver):
        self.dr = driver
        self.chpg = controlcenterpage.CloudHostPage(self.dr)
        self.log = log.Log()

    def into_pv_cloudhost(self):
        try:
            self.chpg.mova_to_menu_bar()
            self.chpg.move_to_project_view_button()
            self.chpg.click_project_view_button()
            sleep(2)
            # self.chpg.click_cloud_host_snap_button()
            # self.chpg.move_to_project_cloud_host_button()

            self.chpg.click_control_center_button()
        except  Exception as e:
            self.log.error("进入云主机模块失败：%s"%e)


if __name__ == '__main__':
    from public.common import pyselenium
    from config import globalparam
    from public.appmodel.loginaction import Login

    dr = pyselenium.PySelenium(globalparam.browser)
    dr.max_window()
    login = Login(dr).login("hubei01", "1qaz!QAZ")
    ch = CloudHostAction(dr)
    ch.into_pv_cloudhost()
    sleep(1)
    dr.quit()



