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
        self.dr.type_and_enter("xpath=(//input[@type='text'])[12]",value)

