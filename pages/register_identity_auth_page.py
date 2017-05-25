#coding:utf-8
from functions.BasePage import BasePage
from selenium.webdriver.common.by import By
from pages.home_page import HomePage

class RegisterIdentityAuthPage(BasePage):
    context="register identity auth page"

    #姓名文本输入框元素
    @property
    def el_name_text_input(self):
        return self.base_find_element(By.ID,"com.quarkfinance.ufo:id/edit_phone")

    #身份证文本输入框  元素
    @property
    def el_id_text_input(self):
        return self.base_find_element(By.ID,"com.quarkfinance.ufo:id/edit_yanzheng")

    #邮箱文本输入框 元素
    @property
    def el_email_text_input(self):
        return self.base_find_element(By.ID,"com.quarkfinance.ufo:id/edit_email")

    #下一步按钮 元素
    @property
    def el_next_step_btn(self):
        return self.base_find_element(By.ID,"com.quarkfinance.ufo:id/tv_nextstep")

    def logic_entry_user_info(self,name,id,email):
        self.el_name_text_input.send_keys(name)
        self.el_id_text_input.send_keys(id)
        self.el_email_text_input.send_keys(email)
        self.el_next_step_btn.click()
        return HomePage(self.driver)

    #跳转至home_page(首页)
    def logic_link_home_page(self):
        self.el_next_step_btn.click()
        return HomePage(self.driver)