#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/30 9:07
# @Author  : mrwuzs
# @Site    :
# @File    : test_14_delete_tenant_user.py
# @Software: PyCharm
import pytest
import allure

from public.common import mytest
from public.common import datainfo
from public.appModel import userAction
from public.pages import authUserPage
from public.appModel.loginAction import Login


@allure.feature("用户管理")
class TestDeleteUser(mytest.MyTest):
    """删除运营部门下的用户测试"""

    @allure.story("删除运营部门下的用户")
    @pytest.mark.flaky(reruns=3)
    def test_delete_tenant_user(self):

        login = Login(self.dr)
        datas = datainfo.get_xls_to_dict("user.xlsx", "Sheet1")[0]
        data1s = datainfo.get_xls_to_dict("user.xlsx", "authuser")[0]
        aupg = authUserPage.AuthUsertPage(self.dr)
        ta = userAction.UserAction(self.dr)
        # t_data = datainfo.get_xls_to_dict("tenantdata.xlsx","Sheet1")[0]
        login.login(datas["username"], datas["password"])
        # ta.create_tenant_user(data1s["tenantname"],data1s["username"],data1s["firstname"],data1s["password"],data1s["repassword"],data1s["email"])
        ta.delete_tenant_user(data1s["username"])
        aupg.open_authuser()

        aupg.input_select_user(data1s["username"])
        self.dr.wait(5)
        self._add_image("删除运营部门下的用户")
        flag = self.dr.element_exist("xpath->//td")
        assert flag is False

        # text = self.dr.get_text("xpath->//div[@class='box-body']/table-component/div/table/tbody")
        # print(text)


if __name__ == "__main__":
    pytest.main(["-s", "test_14_delete_tenant_user.py"])
