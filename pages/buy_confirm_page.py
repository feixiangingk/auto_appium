#coding:utf-8
from functions.BasePage import BasePage
from selenium.webdriver.common.by import By
from pages.buy_trade_result_page import BuyTradeResultPage
import time


class BuyConfirmPage(BasePage):

    context="buy confirm page"

    #"确认支付"按钮 元素
    @property
    def el_buy_btn(self):
        return self.base_find_element(By.XPATH,"//android.widget.TextView[contains(@text,'确认支付')]")

    #弹出框"请输入登录密码" 元素
    @property
    def el_password_text_input(self):
        return self.base_find_element(By.ID,"com.quarkfinance.ufo:id/edit_password")

    #弹出框"确定"按钮  元素
    @property
    def el_confirm_btn(self):
        return self.base_find_element(By.XPATH,"//android.widget.TextView[contains(@text,'确定')]")

    #页面逻辑封装，点击立即投资，输入登录密码，点击确定按钮
    def logic_confirm_info(self,pwd='qwe123'):
        time.sleep(0.5)
        self.el_buy_btn.click()
        self.el_password_text_input.send_keys(pwd)
        self.el_confirm_btn.click()
        return BuyTradeResultPage(self.driver)


    def logic_link_confirm(self):
        self.el_confirm_btn.click()
        return BuyTradeResultPage(self.driver)