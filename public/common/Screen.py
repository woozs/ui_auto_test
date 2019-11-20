#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/7 11:47
# @Author  : mrwuzs
# @Site    : 
# @File    : Screen.py
# @Software: PyCharm
from public.common import publicfunction
from functools import wraps
from public.common import log

class Screen(object):
    """失败截图装饰器"""

    def __init__(self, driver):
        self.driver = driver
        self.log  = log.Log()

    def __call__(self, func):
        @wraps(func)
        def inner(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
            except:
                publicfunction.get_img(self.driver,func.__name__)
            else:
                self.log.info(" %s 脚本运行正常" %func.__name__)

            return result

        return inner
