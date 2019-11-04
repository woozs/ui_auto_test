#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/24 15:19
# @Author  : mrwuzs
# @Site    : 
# @File    : userAction.py
# @Software: PyCharm
import allure

from time import sleep
from public.pages import sysUorgMgrPage,sysMorgMgrPage,authUserPage
from public.common import log

class UserAction(object):
    def __init__(self, driver):
        self.dr = driver
        self.userpage =sysUorgMgrPage.SysUorgMgrPage(self.dr)
        self.mgrpage = sysMorgMgrPage.SysMorgMgrPage(self.dr)
        self.a_u_pg =  authUserPage.AuthUsertPage(self.dr)
        self.log = log.Log()


    def create_user(self,mgrname,username,firstname,password,repassword,email):
        with allure.step("创建用户"):
            allure.attach("域名称：%s"%mgrname)
            allure.attach("用户名:%s"%username)
            allure.attach("密码:%s"%password)
            allure.attach("电邮箱:%s"%email)
        self.userpage.open_uorgmgrpage()
        sleep(1)
        self.userpage.click_new_user_buttun()
        self.userpage.click_select_mgr()
        self.userpage.click_mgr(mgrname)
        self.userpage.input_usrname(username)
        self.userpage.input_firstname(firstname)
        self.userpage.input_first_password(password)
        self.userpage.input_repassword(repassword)
        self.userpage.input_email(email)
        self.userpage.click_save_user_buttun()

    def delete_user(self,username):
        with allure.step("删除用户"):
            allure.attach("用户名：%s" % username)
        self.userpage.open_uorgmgrpage()
        self.userpage.input_select_user(username)
        sleep(0.5)
        self.userpage.click_user_more_button()
        sleep(0.5)
        self.userpage.click_user_delete_button()
        sleep(0.5)
        self.userpage.click_user_delete_success_button()





    def allocation_domain_administrator(self,mgrname,username):
        with allure.step("给域分配管理员"):
            allure.attach("域名称：%s" % mgrname)
            allure.attach("用户名:%s" % username)
        self.mgrpage.open_sys_morg_mgr_page()
        self.mgrpage.select_mgr(mgrname)
        self.mgrpage.click_general_post()
        self.mgrpage.click_user_buttun()
        self.mgrpage.click_seletc_user()
        sleep(2)
        self.mgrpage.search_user(username)
        sleep(2)
        self.mgrpage.click_search_user()
        self.mgrpage.click_save_user()

    def remove_domain_administrator(self,mgrname,username):
        with allure.step("给域移除管理员"):
            allure.attach("域名称：%s" % mgrname)
            allure.attach("用户名:%s" % username)
        self.mgrpage.open_sys_morg_mgr_page()
        self.mgrpage.select_mgr(mgrname)
        self.mgrpage.click_general_post()
        self.mgrpage.click_user_buttun()
        self.mgrpage.input_and_search_user(username)
        self.mgrpage.click_remove_user_button()
        self.mgrpage.click_remove_user_success_button()




    def create_tenant_user(self,tenantname,username,firstname,password,repassword,email):
        """
        在运营部门下创建用户
        :param tenantname:
        :param username:
        :param firstname:
        :param password:
        :param repassword:
        :param email:
        :return:
        """
        with allure.step("运营部门下创建用户"):
            allure.attach("运营部门：%s" % tenantname)
            allure.attach("用户名:%s" % username)
            allure.attach("密码:%s" % password)
            allure.attach("电邮箱:%s" % email)
        self.a_u_pg.open_authuser()
        sleep(1)
        self.a_u_pg.click_crate_user_button()
        self.a_u_pg.click_selcet_tenant()
        sleep(1)
        # self.dr.select_element()
        self.a_u_pg.input_select_tenant(tenantname)
        sleep(1)
        self.a_u_pg.click_radio_tenant_name()
        self.a_u_pg.click_commit_button()
        self.a_u_pg.input_username(username)
        self.a_u_pg.input_firstname(firstname)
        self.a_u_pg.input_password(password)
        self.a_u_pg.input_repassword(repassword)
        self.a_u_pg.input_email(email)
        self.a_u_pg.click_new_user_save_button()


        # self.dr.click("xpath -> /html/body/div[@id='addUserModal']/"
        #               "div/div/div/form/table-component/div/table"
        #               "/tbody/tr[@class='ng-scope']/"
        #               "tr[@class='width20 text-center ng-scope']/"
        #               "div[@class='checker']/input[@type='radio']")

    def delete_tenant_user(self,username):
        with allure.step("删除运营部门用户"):
            allure.attach("用户名：%s" % username)
        self.a_u_pg.open_authuser()
        sleep(1)
        self.a_u_pg.input_select_user(username)
        sleep(2)
        self.a_u_pg.click_user_more_button()
        sleep(0.5)
        self.a_u_pg.click_user_delete_button()
        sleep(0.5)
        self.a_u_pg.click_user_delete_success_button()




if __name__ == '__main__':
    from public.common import pyselenium
    from config import globalparam
    from public.appModel.loginAction import Login

    dr = pyselenium.PySelenium(globalparam.browser)
    dr.max_window()
    login = Login(dr).login("系统管理员", "123456")

    #
    user =UserAction(dr)
    #
    # # user.create_user("河南","wuzs0001","wuzs0001","1qaz!QAZ","1qaz!QAZ","wzs@qq.com")
    # user.create_tenant_user("wuzs_auto01", "wuzs_teant_0001", "wuzs_teant_0001", "1qaz!QAZ", "1qaz!QAZ", "wzs@qq.com")
    # user.allocation_domain_administrator("河南","wuzs0001")
    user.remove_domain_administrator("河南","wuzs_auto_0001")
    sleep(2)
    dr.quit()
    #