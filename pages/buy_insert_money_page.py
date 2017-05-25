#coding:utf-8

from functions.BasePage import BasePage
from selenium.webdriver.common.by import By
from pages.buy_confirm_page import BuyConfirmPage

class BuyInsertMoneyPage(BasePage):

    context='buy insert money page'

    #金额输入框 元素
    @property
    def el_amount_text_input(self):
        return self.base_find_element(By.XPATH,"//android.widget.EditText[contains(@resource-id,'com.quarkfinance.ufo:id/edit_amount')]")

    #同意协议单选框 元素
    @property
    def el_checkBox_btn(self):
        return  self.base_find_element(By.XPATH,"//android.widget.CheckBox")

    #立即支付按钮 元素
    @property
    def el_buy_btn(self):
        return self.base_find_element(By.XPATH,"//android.widget.TextView[contains(@text,'立即支付')]")

    def logic_buy_product(self,money):
        self.el_amount_text_input.send_keys(str(money))
        self.el_checkBox_btn.click()
        self.el_buy_btn.click()
        return BuyConfirmPage(self.driver)

    def logic_link_buy(self):
        self.el_buy_btn.click()
        return BuyConfirmPage(self.driver)