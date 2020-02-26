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
from public.common.mysql_pub import OpMysql


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

def get_project_id(projectname):
    user = OpMysql('192.168.253.55',14316,'arkproxy','P@ssw0rd','user')
    uuid = user.select_one("SELECT UUID FROM project WHERE NAME  LIKE '%s' "%projectname)["UUID"]
    return uuid


if __name__ == '__main__':
    from public.common import pyselenium
    # dr = pyselenium.PySelenium(globalparam.browser)
    # dr.max_window()
    # dr.open('http://192.168.54.13/#/login')
    # get_img(dr, "登录界面")
    print(get_project_id("湖北"))
