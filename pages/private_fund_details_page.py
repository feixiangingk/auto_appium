#coding:utf-8

from functions.BasePage import BasePage
from functions.appium_init import *
from selenium.webdriver.common.by import By

class Private_Fund_Details_Page(BasePage):
    "私募详情页"



    @property
    def el_title_text(self):
        return self.base_find_element(By.ID, "com.quarkfinance.ufo:id/item_view")

    #确认密码
    @property
    def el_input_password(self):
        return self.base_find_element(By.ID, "com.quarkfinance.ufo:id/edit_password")

    #咨询
    @property
    def el_input_consultation(self):
        return self.base_find_element(By.ID, "com.quarkfinance.ufo:id/text_inquiry")

    #确认提交
    @property
    def el_input_btn(self):
        return self.base_find_element(By.ID, "com.quarkfinance.ufo:id/text_confirm_btn")




    #预约成功提示文本
    @property
    def el_text_message_text(self):
        return self.base_find_element(By.ID, "com.quarkfinance.ufo:id/text_message")


    #预约成功确认
    @property
    def el_confirm_btn(self):
        return self.base_find_element(By.ID, "com.quarkfinance.ufo:id/text_confirm_btn")



