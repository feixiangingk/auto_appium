#coding:utf-8
from functions.BasePage import BasePage
from selenium.webdriver.common.by import By
from pages.buy_insert_money_page import BuyInsertMoneyPage
from appium.webdriver.common.touch_action import TouchAction
import time

class ProductBeautiPage(BasePage):

    context='product beauti page'


    #"立即投资"按钮 元素
    @property
    def el_buy_btn(self):
        return self.base_find_element(By.XPATH,"//android.widget.TextView[contains(@text,'立即投资')]")


    #title
    @property
    def el_title_text(self):
        return self.base_find_element(By.ID, "com.quarkfinance.ufo:id/tb_title")




    #非登录态点击立即投资按钮，跳转至登录页
    def logic_noLogin_state_buy(self):
        from pages.login_page import LoginPage
        self.el_buy_btn.click()
        return LoginPage(self.driver)

    #跳转buy_insert_money_page页面
    def logic_link_buy(self):
        self.el_buy_btn.click()
        return BuyInsertMoneyPage(self.driver)


    def logic_get_title_text(self):
        title=self.el_title_text.text
        return title