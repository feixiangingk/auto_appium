#coding:utf-8
from functions.BasePage import BasePage
from selenium.webdriver.common.by import By
from pages.register_patternlock_page import  RegisterPatternlockPage

class RegisterReferencePage(BasePage):
    context="register reference page"

    #"忽略"按钮  元素
    @property
    def el_hulue_btn(self):
        return self.base_find_element(By.ID,"com.quarkfinance.ufo:id/tv_hulue")

    #点击忽略按钮，跳转register_patternlock_page
    def logic_link_hulue(self):
        self.el_hulue_btn.click()
        return RegisterPatternlockPage(self.driver)

