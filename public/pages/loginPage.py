#coding=utf-8

from public.common import basepage
from config import globalparam


class LoginPage(basepage.Page):

    def into_cmp_page(self):
        """打开百度首页"""
        self.dr.open(globalparam.url)


    def input_username(self,values):
        """输入用户名"""
        self.dr.clear_type("xpath -> //input[@name='username']",values )

    def input_password(self,values):
        """输入用户名"""
        self.dr.clear_type("xpath -> //input[@name='password']",values )

    def input_code(self,valuses):
        """
        输入验证码
        :param valuses:
        :return:
        """
        self.dr.clear_type("xpath -> //input[@name='captcha']",valuses)

    def  click_loginbutton(self):
        '''
        点击登录按钮
        :return: 
        '''''
        self.dr.click("xpath -> //button[contains(.,'登录')]")

    
    # def input_search_key(self, values):
    #     """输入搜索关键词"""
    #     self.dr.clear_type('id->kw', values)
    #
    # def click_search_button(self):
    #     """点击搜索按钮"""
    #     self.dr.click('id->su')
    #
    # def return_title(self):
    #     """返回该页面的title"""
    #     return self.dr.get_title()

