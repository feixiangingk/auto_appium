#coding:utf-8
from functions.BasePage import BasePage
from functions.appium_init import *
from selenium.webdriver.common.by import By
from pages.product_quarkzx_page import ProductQuarkzxPage

class ProductListPage(BasePage):

    context='product list page'

    #夸客尊享按钮 元素
    @property
    def el_quarkZX_btn(self):
        return self.base_find_element(By.XPATH,"//android.widget.TextView[contains(@text,'夸客尊享')]")

    #点击夸客尊享链接，跳转至夸客尊享产品详情page
    def logic_link_quarkZX(self):
        self.el_quarkZX_btn.click()
        return ProductQuarkzxPage(self.driver)