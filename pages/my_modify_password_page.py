#coding:utf-8

import time,sys
reload(sys)
sys.setdefaultencoding('utf-8')

from functions.BasePage import BasePage
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage


class Modify_Password_page(BasePage):
    "个人中心-修改密码页面"


    #当前密码
    @property
    def el_current_pass_text(self):
        return self.base_find_element(By.ID,"com.quarkfinance.ufo:id/edit_current_pass")


    # 新密码
    @property
    def el_password_text(self):
        return self.base_find_element(By.ID, "com.quarkfinance.ufo:id/edit_password")

    # 再次输入
    @property
    def el_reinput_pass_text(self):
        return self.base_find_element(By.ID, "com.quarkfinance.ufo:id/edit_reinput")


    # 提交修改
    @property
    def el_nextstep_btn(self):
        return self.base_find_element(By.ID, "com.quarkfinance.ufo:id/tv_nextstep")


    def logic_nextstep_btn_click(self):
        self.el_nextstep_btn.click()
        return LoginPage(self.driver)