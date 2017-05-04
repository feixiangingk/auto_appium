#coding:utf-8
from pages.base_page import BasePage
from pages.my_page import MyPage

class HomePage(BasePage):

    context='im home page'

    #定位器:首页
    @property
    def home_btn(self):
        return self.by_name(u'首页')

    #定位器：我的
    @property
    def my_btn(self):
        return self.by_name(u'我的')

    #定位器：产品列表
    @property
    def product_btn(self):
        return self.by_name(u'产品列表')



    #逻辑key_word:跳转到"我的"页面
    def my_page(self):
        self.my_btn.click()
        return MyPage(self.driver)

    #逻辑key_word:跳转到"产品列表"页面
    def product_page(self):
        self.product_btn.click()
