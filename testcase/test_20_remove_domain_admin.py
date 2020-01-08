#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/31 9:32
# @Author  : mrwuzs
# @Site    :
# @File    : test_20_remove_domain_admin.py
# @Software: PyCharm
import pytest
import allure

from time import sleep
from public.common.publicfunction import *
from public.common import datainfo
from public.appmodel import useraction
from public.pages import sysUorgMgrPage
from public.appmodel.loginaction import Login


@pytest.mark.usefixtures("driver")
@pytest.mark.usefixtures('login_admin')
@allure.feature("域管理")
class TestRemoveDomainAdmin():
    """移除域管理员"""

    @allure.story("移除域管理员")
    @pytest.mark.flaky(reruns=3)
    def test_remove_domain_admin(self,login_admin):

        dr = login_admin
        datas = datainfo.get_xls_to_dict("user.xlsx", "Sheet1")["创建域管理员"]
        upage = sysUorgMgrPage.SysUorgMgrPage(dr)
        ua = useraction.UserAction(dr)
        ua.remove_domain_administrator(datas["mgrname"], datas["username"])
        # 校验已分配域管理角色
        upage.open_uorgmgrpage()
        upage.input_select_user(datas["username"])
        sleep(2)
        dr.wait(5)
        add_image(dr,"移除域管理员")
        character = dr.get_text(
            "css->.ng-scope:nth-child(4) > .wordBreak")
        assert character == "0"


if __name__ == "__main__":
    pytest.main(["-s", "test_20_remove_domain_admin.py"])
