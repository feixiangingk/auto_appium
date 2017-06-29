#coding=utf-8

import time
from selenium.webdriver.common.by import By
from functions.BasePage import BasePage
from functions.appium_init import *
from pages.startup_page import StartupPage
from pages.register_choose_page import RegisterChoosePage


class Forget_Pass(BasePage):
    "忘记密码"

    #手机号
    @property
    def el_edit_phone(self):
        return self.base_find_element(By.ID,"com.quarkfinance.ufo:id/edit_phone")

    # 获取验证码
    @property
    def el_get_verify(self):
        return self.base_find_element(By.ID, "com.quarkfinance.ufo:id/tv_getverify")

    # 输入验证码
    @property
    def el_edit_yanzheng(self):
        return self.base_find_element(By.ID,  "com.quarkfinance.ufo:id/edit_yanzheng")


    # 提交
    @property
    def el_tv_nextstepself(self):
        return self.base_find_element(By.ID, "com.quarkfinance.ufo:id/tv_nextstep")



    #输入新密码
    @property
    def el_edit_password(self):
        return self.base_find_element(By.ID,"com.quarkfinance.ufo:id/edit_password")

    # 输入新密码
    @property
    def el_edit_reinput(self):
        return self.base_find_element(By.ID, "com.quarkfinance.ufo:id/edit_reinput")

    #title
    @property
    def el_tb_title(self):
        return self.base_find_element(By.ID, "com.quarkfinance.ufo:id/tb_title")




    #找回密码最后一步，返回login page
    def logic_tv_nextstepself_click(self):
        from pages.login_page import LoginPage
        self.el_tv_nextstepself.click()
        return LoginPage(self.driver)










