#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/1 21:38
# @Author  : mrwuzs
# @Site    :
# @Software: PyCharm

import os
import time
from config import globalparam


# 截图放到report下的img目录下
def get_img(dr, filename):
    if not os.path.exists(globalparam.img_path ):
        os.makedirs(globalparam.img_path )
    path = globalparam.img_path + '\\' + filename + \
        '_' + time.strftime('%Y_%m_%d_%H_%M_%S') + '.png'
    # path = globalparam.img_path + '\\' + filename + '.png'
    dr.take_screenshot(path)

    return path





if __name__ == '__main__':
    from public.common import pyselenium
    dr = pyselenium.PySelenium(globalparam.browser)
    dr.max_window()
    dr.open('http://192.168.54.13/#/login')
    get_img(dr, "登录界面")
