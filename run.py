# coding=utf-8

#!/usr/bin/env.ini python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/11 15:34
# @Author  : mrwuzs
# @Site    :
# @File    : run.py
# @Software: PyCharm


"""
运行用例集：
    python3 run.py

# '--allure_severities=critical, blocker'
# '--allure_stories=测试模块_demo1, 测试模块_demo2'
# '--allure_features=测试features'

"""

import pytest

from public.common import log
from public.common import shell
from public.common import initialize_Env
from config import globalparam


failureException = AssertionError

if __name__ == '__main__':

    log = log.Log()

    shell = shell.Shell()
    xml_report_path = globalparam.xml_report_path
    html_report_path = globalparam.html_report_path

    # 初始化allure环境配置文件environment.xml
    initialize_Env.Init_Env().init()

    # 定义测试集
    args = ['-s', '-q', '--alluredir', xml_report_path]
    # args = ['-s', '-q', '--alluredir', "H:\\api_auto_test\\Report\xml"]
    pytest.main(args)
    cmd = 'allure generate %s -o %s  --clean' % (
        xml_report_path, html_report_path)
    log.info("执行allure，生成测试报告")
    try:
        shell.invoke(cmd)
    except Exception:
        log.error('执行用例失败，请检查环境配置')
        raise
    print("报告已生成，请查看")
