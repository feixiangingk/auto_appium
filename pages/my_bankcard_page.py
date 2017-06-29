#coding:utf-8
from functions.BasePage import BasePage
from selenium.webdriver.common.by import By
from pages.register_addcard_page import RegisterAddCardPage
import time

class MyBankCardPage(BasePage):

    context='my bankcard page'

    #我的银行卡页面新增银行卡按钮 元素
    @property
    def el_addCard_btn(self):
        return self.base_find_element(By.ID,"com.quarkfinance.ufo:id/tb_right")

    @property
    def el_bankcard_list(self):
        return self.base_find_elements(By.ID,"com.quarkfinance.ufo:id/ll_bank_layout")


    #银行卡列表第一个元素
    @property
    def el_bankName_listOne(self):
        return self.base_find_elements(By.ID,"com.quarkfinance.ufo:id/tv_bankname")[0]

    #银行卡尾号第一个元素
    @property
    def el_bankWeihao_listOne(self):
        return self.base_find_elements(By.ID,"com.quarkfinance.ufo:id/tv_weihao")[0]


    def logic_addCard_click(self):
        self.el_addCard_btn.click()
        return RegisterAddCardPage(self.driver)




