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

    