#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/1 21:38
# @Author  : mrwuzs
# @Site    :
# @Software: PyCharm

"""
封装Assert方法

"""
from public.common.log import Log
from public.common import Consts
import json


class Assertions:
    def __init__(self):
        self.log = Log()

    def assert_in_text(self, body, expected_msg):
        """
        验证response body中是否包含预期字符串
        :param body:
        :param expected_msg:
        :return:
        """
        try:
            text = json.dumps(body, ensure_ascii=False)
            # print(text)
            assert expected_msg in text
            return True

        except BaseException:
            self.log.error(
                "Response body Does not contain expected_msg, expected_msg is %s" %
                expected_msg)
            Consts.RESULT_LIST.append('fail')

            raise

    def assert_text(self, body, expected_msg):
        """
        验证response body中是否等于预期字符串
        :param body:
        :param expected_msg:
        :return:
        """
        try:
            assert body == expected_msg
            return True

        except BaseException:
            self.log.error(
                "Response body != expected_msg, expected_msg is %s, body is %s" %
                (expected_msg, body))
            Consts.RESULT_LIST.append('fail')

            raise

    def assert_Ture(self, flag, expected_time):
        """
        验证response body响应时间小于预期最大响应时间,单位：毫秒
        :param body:
        :param expected_time:
        :return:
        """
        try:
            assert flag is True
            return True

        except BaseException:
            self.log.error(
                "Restimeponse  > expected_time, expected_time is %s, time is %s" %
                (expected_time, time))
            Consts.RESULT_LIST.append('fail')

            raise


if __name__ == '__main__':
    AS = Assertions()
    AS.assert_code(203, 203)
