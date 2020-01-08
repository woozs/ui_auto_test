# coding=utf-8

#!/usr/bin/env.ini python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/11 15:34
# @Author  : mrwuzs
# @Site    :
# @File    : run.py
# @Software: PyCharm

import pytest

from public.common import log
from public.common import shell
from public.common import initializeEnv
from config import globalparam
from pyvirtualdisplay import Display


failureException = AssertionError

if __name__ == '__main__':

    log = log.Log()
    shell = shell.Shell()
    xml_report_path = globalparam.xml_report_path
    html_report_path = globalparam.html_report_path

    # 初始化allure环境配置文件environment.xml
    initializeEnv.Init_Env().init()
    # 定义测试集
    args = ['-s', '-q', '--alluredir', xml_report_path]
    pytest.main(args)
    cmd = 'allure generate %s -o %s --clean' % (
        xml_report_path, html_report_path)
    log.info("执行allure，生成测试报告")
    log.debug(cmd)
    try:
        log.info("执行allure")
        shell.invoke(cmd)
    except Exception:
        log.error('执行用例失败，请检查环境配置')
        raise
    # 解决历史趋势中无数据问题
    report_history_path = html_report_path + "\\history"
    result_history_path = xml_report_path + "\\history"
    copy_cmd = 'xcopy %s %s  /e /Y /I' % (report_history_path,
                                          result_history_path)
    try:
        log.info("复制历史数据")
        shell.invoke(copy_cmd)
    except Exception:
        log.error('复制文件失败，请查看失败原因')
        raise
    log.info("报告已生成，请查看")


