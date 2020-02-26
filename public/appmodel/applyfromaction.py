# -*- coding: utf-8 -*-
# @Time    : 2020/2/20 15:27
# @Author  : mrwuzs
# @Email   : mrwuzs@outlook.com
# @File    : applyfromaction.py
# @Software: PyCharm
from  public.pages import controlcenterpage
from  time import sleep


def submission_apply_from(project_name,dr):
    pass




if __name__ == '__main__':
    from public.common import pyselenium
    from config import globalparam
    from public.appmodel.loginaction import Login

    dr = pyselenium.PySelenium(globalparam.browser)
    dr.max_window()
    login = Login(dr).login("hubei01", "1qaz!QAZ")
    submission_apply_from("湖北",dr)




