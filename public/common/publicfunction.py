#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/1 21:38
# @Author  : mrwuzs
# @Site    :
# @Software: PyCharm

import os
import time
import allure
from config import globalparam


# 截图放到report下的img目录下
def get_img(dr, filename):
    if not os.path.exists(globalparam.img_path):
        os.makedirs(globalparam.img_path)
    path = globalparam.img_path + '\\' + filename + \
        '_' + time.strftime('%Y_%m_%d_%H_%M_%S') + '.png'
    # path = globalparam.img_path + '\\' + filename + '.png'
    dr.take_screenshot(path)

    return path


def add_image(dr, filename):
    image_tmp = get_img(dr, filename)
    with open(image_tmp, mode='rb') as f:
        file = f.read()
        allure.attach(file, filename, allure.attachment_type.PNG)


def is_Chinese(char):
    for i in char:
        if u'\u4e00' <= i <= u'\u9fff':
            return True
        else:
            return False


if __name__ == '__main__':
    from public.common import pyselenium
    dr = pyselenium.PySelenium(globalparam.browser)
    dr.max_window()
    dr.open('http://192.168.54.13/#/login')
    get_img(dr, "登录界面")
