# -*- coding: utf-8 -*-
# @Time    : 2019/12/11 9:04
# @Author  : mrwuzs
# @Email   : mrwuzs@outlook.com
# @File    : logoutaction.py
# @Software: PyCharm

import allure

from time import sleep
from public.pages import basepage


class Logout(object):

    def __init__(self, driver):
        self.dr = driver

    @allure.step("退出系统")
    def logout(self):

        try:
            bspage = basepage.Page(self.dr)
            bspage.move_to_el_icon_right()
            sleep(2)
            bspage.click_logout_button()
        except Exception as e:
            raise e


if __name__ == '__main__':
    from public.common import pyselenium
    from config import globalparam
    from public.common import cookiesAction

    dr = pyselenium.PySelenium(globalparam.browser)
    dr.max_window()
    dr.open('http://192.168.54.13/#/login')
    dr = cookiesAction.add_cookie(dr)
    dr.open('http://192.168.54.13/csdp/portal/#/resourceUsage')
    logout = Logout(dr)
    logout.logout()

