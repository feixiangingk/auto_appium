#coding:utf-8
from functions.BasePage import BasePage
from selenium.webdriver.common.by import By
from pages.register_reference_page import RegisterReferencePage
class RegisterPasswordPage(BasePage):
    context="register password page"

    #密码文本输入框 元素
    @property
    def el_password_text_input(self):
        return self.base_find_element(By.ID,"com.quarkfinance.ufo:id/edit_password")

    #再次输入文本输入框 元素
    @property
    def el_password_re_text_input(self):
        return self.base_find_element(By.ID,"com.quarkfinance.ufo:id/edit_reinput")

    #下一步按钮 元素
    @property
    def el_next_step_btn(self):
        return self.base_find_element(By.ID,"com.quarkfinance.ufo:id/tv_nextstep")

    def logic_entry_pwd(self):
        self.el_password_text_input.send_keys('123456q')
        self.el_password_re_text_input.send_keys('123456q')
        self.el_next_step_btn.click()
        return RegisterReferencePage(self.driver)

    #跳转至register_reference_page
    def logic_link_next(self):
        self.el_next_step_btn.click()
        return RegisterReferencePage(self.driver)

