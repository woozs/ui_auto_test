#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/31 9:36
# @Author  : mrwuzs
# @Site    : 
# @File    : test_21_delete_user.py
# @Software: PyCharm
import pytest
import allure

from public.common import mytest
from public.common import datainfo
from public.appModel import userAction
from public.pages import sysUorgMgrPage
from public.appModel.loginAction import Login

@allure.feature("用户管理")
class TestDeleteUser(mytest.MyTest):

    """测试删除域管理员"""
    @allure.story("删除域用户")
    @pytest.mark.flaky(reruns=3)
    def test_delete_user(self):

        login = Login(self.dr)
        login.login("系统管理员",'123456')

        datas = datainfo.get_xls_to_dict("user.xlsx", "Sheet1")[0]
        upage = sysUorgMgrPage.SysUorgMgrPage(self.dr)
        ua = userAction.UserAction(self.dr)
        ua.delete_user(datas["username"])
        # ua.delete_user(datas["username"])
        # upage.input_select_user(datas["username"])
        #查看用户，进行校验
        upage.input_select_user(datas["username"])
        flag = self.dr.element_exist("xpath->//span[contains(.,'%s')]" % datas["username"])
        assert flag is flag,"用户删除成功，请查看日志"


if __name__ == "__main__":
    pytest.main(["-s", "test_21_delete_user.py"])