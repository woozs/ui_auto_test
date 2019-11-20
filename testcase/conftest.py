#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/7 14:21
# @Author  : mrwuzs
# @Site    : 
# @File    : conftest.py
# @Software: PyCharm


import pytest
import allure
from public.appModel import loginAction

@allure.step("登录系统")
@pytest.fixture()
def login():
    print('\n---------------conftest文件login方法开始执行----------------------------')
    print()
    print()
    print('----------------conftest.py文件login方法执行结束---------------------------')


