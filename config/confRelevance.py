#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/2 13:02
# @Author  : mrwuzs
# @Site    : 
# @File    : confRelevance.py
# @Software: PyCharm
import configparser

from public.common.log import Log



class ConfRelevance:
    # 关联文件读取配置
    def __init__(self, _path,title):
        self.log = Log()
        self.log.info("初始化关联文件")
        config = configparser.ConfigParser()
        config.read(_path, encoding="utf-8")
        self.host = config[title]

    def get_relevance_conf(self):
        relevance = dict()
        self.log.debug("读取初始关联文件内容：   %s" % self.host.items())
        for key, value in self.host.items():
            relevance[key] = value
        return relevance



if __name__ == "__main__":
    host = ConfRelevance("H:\\cmp\\config\\config.ini","test")
    print(host.get_relevance_conf())
