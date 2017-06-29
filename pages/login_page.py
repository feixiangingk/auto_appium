#coding=utf-8

import time
from selenium.webdriver.common.by import By
from functions.BasePage import BasePage
from functions.appium_init import *
from pages.startup_page import StartupPage
from pages.register_choose_page import RegisterChoosePage
from pages.my_forget_pass_page import Forget_Pass


class LoginPage(BasePage):

    context='im login page'

#new  PO  return element

#登录页面没有该元素，删除
    # @property
    # def el_my_btn(self):
    #     return self.base_find_element(By.NAME,u'我的')

    #登录页title
    @property
    def el_title(self):
        return self.base_find_element(By.ID,"com.quarkfinance.ufo:id/tb_title")

    #手机号 文本输入框 元素
    @property
    def el_phone_text_input(self):
        return self.base_find_element(By.ID,"com.quarkfinance.ufo:id/edit_name")

    #密码 文本输入框 元素
    @property
    def el_pwd_text_input(self):
        return self.base_find_element(By.ID,"com.quarkfinance.ufo:id/edit_password")

    #登录按钮 元素
    @property
    def el_login_btn(self):
        return  self.base_find_element(By.ID,"com.quarkfinance.ufo:id/tv_login")

    #注册按钮 元素
    @property
    def el_register_btn(self):
        return self.base_find_element(By.XPATH,"//android.widget.TextView[contains(@text,'注册')]")

    #忘记密码 元素
    @property
    def el_forget_pass(self):
        return  self.base_find_element(By.ID, "com.quarkfinance.ufo:id/tv_forget_pass")


    #点击跳转至register_sms_page页面
    def logic_link_register(self):
        self.el_register_btn.click()
        return RegisterChoosePage(self.driver)


    #逻辑方法-登录
    def logic_login(self,phone='14488888098',pwd='qwe123'):
            """
             :param phone: 账户
             :param pwd:  密码
              :return:  HomePage
            """

            from pages.home_page import HomePage
            self.el_phone_text_input.send_keys(phone)
            self.el_pwd_text_input.send_keys(pwd)
            self.el_login_btn.click()
            #time.sleep(3)
            return HomePage(self.driver)

    #点击忘记密码
    def logic_el_forget_pass_click(self):
        self.el_forget_pass.click()
        return Forget_Pass(self.driver)





if __name__ == '__main__':
    # info = Initialization()
    Init()
    driver = appium_init.inital.get_driver()
    d = LoginPage(driver)
    #d.logic_login('18048444414','hele5201')
    time.sleep(2)

