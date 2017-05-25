#coding:utf-8
from functions.BasePage import BasePage
from selenium.webdriver.common.by import By
from pages.register_sms_page import RegisterSmsPage
class RegisterChoosePage(BasePage):
    context='register choose page'

    #"新客户"按钮 元素
    @property
    def el_new_user_btn(self):
        return self.base_find_element(By.XPATH,"//android.widget.TextView[contains(@text,'新客户')]")

    #点击跳转至register_sms_page页面
    def logic_link_new_user(self):
        self.el_new_user_btn.click()
        return RegisterSmsPage(self.driver)