#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/6 17:58
# @Author  : mrwuzs
# @Site    :
# @File    : cookiesAction.py
# @Software: PyCharm
import json
from public.common import pyselenium
from config import globalparam
from public.appmodel.loginaction import Login
cookie_path = globalparam.cookie_path + "\\cookies.json"


def get_cookie(username, password):
    dr = pyselenium.PySelenium(globalparam.browser)
    dr.max_window()
    Login(dr).login(username, password)
    cookies = dr.origin_driver.get_cookies()
    jsonCookies = json.dumps(cookies)
    with open(cookie_path, 'w') as f:
        f.write(jsonCookies)


def add_cookie(dr):
    dr.origin_driver.delete_all_cookies()
    print(cookie_path)
    with open(cookie_path, 'r', encoding='utf-8') as f:
        listCookies = json.loads(f.read())
    for cookie in listCookies:
        dr.origin_driver.add_cookie({
            'domain': cookie['domain'],
            'name': cookie['name'],
            'value': cookie['value'],
            'path': '/',
            'httpOnly': False,
            'secure': False
        })
    return dr


if __name__ == '__main__':
    get_cookie("系统管理员", "123456")
