#coding:utf-8
from functions.BasePage import BasePage
from selenium.webdriver.common.by import By
from functions.appium_init import *

class MyPersonalCenterPage(BasePage):

    context='my personal center page'

    #手机号文本 元素
    @property
    def el_phone_text(self):
        return self.base_find_element(By.ID,"com.quarkfinance.ufo:id/tv_phonenumber")