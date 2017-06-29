#coding:utf-8
from functions.BasePage import BasePage
from selenium.webdriver.common.by import By


class BuyTradeResultPage(BasePage):

    context='buy trade result page'

    #"确认"按钮 元素
    @property
    def el_confirm_btn(self):
        return self.base_find_element(By.XPATH,"//android.widget.TextView[contains(@text,'确认')]")

    #跳转至首页
    def logic_link_buy(self):
        from pages.home_page import HomePage
        self.el_confirm_btn.click()
        from pages.home_page import HomePage
        return HomePage(self.driver)
