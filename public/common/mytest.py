#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/1 21:38
# @Author  : mrwuzs
# @Site    :
# @Software: PyCharm

import allure
from public.common import pyselenium
from config import globalparam
from public.common.log import Log
from public.appModel.loginAction import Login
from public.common import publicfunction


class MyTest():
    """
    The base class is for all testcase.
    """

    def setup_class(self):
        self.logger = Log()
        self.imge_path = globalparam.img_path
        self.logger.info(
            '############################### START ###############################')
        self.dr = pyselenium.PySelenium(globalparam.browser)
        self.dr.max_window()
        self.login = Login(self.dr)



    def teardown_class(self):
        self.dr.quit()
        self.logger.info(
            '###############################  End  ###############################')

    def _add_image(self,filename):
        image_tmp = publicfunction.get_img(self.dr, filename)
        with  open(image_tmp, mode='rb') as f:
            file = f.read()
            allure.attach(file, filename, allure.attachment_type.PNG)
