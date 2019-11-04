#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/2 12:50
# @Author  : mrwuzs
# @Site    : 
# @File    : shell.py
# @Software: PyCharm


"""
封装执行shell语句方法

"""

import subprocess


class Shell:
    @staticmethod
    def invoke(cmd):
        output, errors = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        o = output.decode("utf-8")
        return o
