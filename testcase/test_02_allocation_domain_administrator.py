#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/25 16:35
# @Author  : mrwuzs
# @Site    :
# @File    : test_02_allocation_domain_administrator.py
# @Software: PyCharm
import pytest
import allure

from time import sleep
from public.common import datainfo
from public.common.publicfunction import *
from public.appmodel import useraction
from public.pages import sysUorgMgrPage

@allure.feature("域管理")
class TestAllDomainAdmin():
    """域添加域管理员"""

    @allure.story("域添加域管理员")
    @pytest.mark.flaky(reruns=3)
    def test_allocation_domain_admin(self,login_admin):
        dr = login_admin
        datas = datainfo.get_xls_to_dict("user.xlsx", "Sheet1")["创建域管理员"]
        upage = sysUorgMgrPage.SysUorgMgrPage(dr)
        ua = useraction.UserAction(dr)
        ua.allocation_domain_administrator(datas["mgrname"], datas["username"])
        # 校验已分配域管理角色
        upage.open_uorgmgrpage()
        upage.input_select_user(datas["username"])
        sleep(2)
        character = dr.get_text(
            "css->.ng-scope:nth-child(4) > .wordBreak")
        add_image(dr,"域添加域管理员")
        assert character == "1"
        # self.assertTrue(dr.element_exist(""]), "用户未创建成功，请查看日志")


if __name__ == "__main__":
    pytest.main(["-s", "test_02_allocation_domain_administrator.py"])
