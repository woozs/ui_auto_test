# coding=utf-8

import  allure
from public.pages import basepage
from config import globalparam


class LoginPage(basepage.Page):

    @allure.step("打开CSDP登录页面")
    def into_cmp_page(self):
        """打开CMP首页"""
        self.log.debug("打开CSDP登录页面")
        self.dr.open(globalparam.url)

    def input_username(self, values):
        """输入用户名"""
        self.log.debug("输入用户名")
        self.dr.clear_type("xpath -> //input[@name='username']", values)

    def input_password(self, values):
        """输入密码"""
        self.log.debug("输入密码")
        self.dr.clear_type("xpath -> //input[@name='password']", values)

    def input_code(self, valuses):
        """
        输入验证码
        :param valuses:
        :return:
        """
        self.log.debug("输入验证码")
        self.dr.clear_type("xpath -> //input[@name='captcha']", valuses)

    def click_loginbutton(self):
        '''
        单击登录按钮
        :return:
        '''''
        self.log.debug("单击登录按钮")
        self.dr.click("xpath -> //button[contains(.,'登录')]")
