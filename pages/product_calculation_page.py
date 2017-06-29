#coding:utf-8
from functions.BasePage import BasePage
from selenium.webdriver.common.by import By

class ProductCalculationPage(BasePage):
    context='product calculation page'

    #计算按钮 元素
    @property
    def el_calculation_btn(self):
        return self.base_find_element(By.ID,"com.quarkfinance.ufo:id/text_calculate")

    #页面title
    @property
    def el_title(self):
        return self.base_find_element(By.ID,"com.quarkfinance.ufo:id/tb_title")