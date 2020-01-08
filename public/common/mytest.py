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
from public.appmodel.loginaction import Login
from public.common import publicfunction


class MyTest():
    """
    The base class is for all testcase.
    """

    def setup_module(module):
        """ setup any state specific to the execution of the given module."""
        print("123544444444444444444444444444444444")



    def teardown_module(module):
        """ teardown any state that was previously setup with a setup_module
        method.
        """
        print("123544444444444444444444444444444444")

    def setup_class(cls):
        cls.logger = Log()
        cls.imge_path = globalparam.img_path
        cls.logger.info(
            '############################### START ###############################')
        cls.dr = pyselenium.PySelenium(globalparam.browser,globalparam.headless)
        cls.dr.max_window()
        cls.login = Login(cls.dr)



    def teardown_class(cls):
        cls.dr.quit()
        cls.logger.info(
            '###############################  End  ###############################')

    def _add_image(self,filename):
        publicfunction.add_image(self.dr,filename)
