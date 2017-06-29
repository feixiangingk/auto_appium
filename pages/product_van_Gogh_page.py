#coding:utf-8
from functions.BasePage import BasePage
from selenium.webdriver.common.by import By
from pages.buy_insert_money_page import BuyInsertMoneyPage
from appium.webdriver.common.touch_action import TouchAction
import time

class ProductVanGoghPage(BasePage):

    context='product van_Gogh page'

    #梵高计划类别(60天 90天 360天)控件
    @property
    def el_product_kind_btn(self):
        return self.base_find_element(By.ID,"com.quarkfinance.ufo:id/pickerView")

    #"立即投资"按钮 元素
    @property
    def el_buy_btn(self):
        return self.base_find_element(By.XPATH,"//android.widget.TextView[contains(@text,'立即投资')]")

        # 选择理财产品小类，比如(30天、60天、90天…… 入参no=1代表选第一个30天，no=2选60天以此类推)

    def logic_choose_product_type(self, no):
        dic_size = self.el_product_kind_btn.size
        dic_loc = self.el_product_kind_btn.location

        position_y = dic_loc['y'] + dic_size['height'] / 2
        self.driver.implicitly_wait(20)
        if no == 1:
            position_x = dic_size['width'] * 0.097
        elif no == 2:
            position_x = dic_size['width'] * 0.3
        elif no == 3:
            position_x = dic_size['width'] * 0.5
        elif no == 4:
            position_x = dic_size['width'] * 0.7
        elif no == 5:
            position_x = dic_size['width'] * 0.9028
        elif no == 6:
            position_x = dic_size['width'] * 0.9028
            TouchAction(self.driver).press(x=position_x, y=position_y).release().perform()
            time.sleep(1)
            position_x = dic_size['width'] * 0.7

        TouchAction(self.driver).press(x=position_x, y=position_y).release().perform()
        time.sleep(1)

    #非登录态点击立即投资按钮，跳转至登录页
    def logic_noLogin_state_buy(self):
        from pages.login_page import LoginPage
        self.el_buy_btn.click()
        return LoginPage(self.driver)

    #跳转buy_insert_money_page页面
    def logic_link_buy(self):
        self.el_buy_btn.click()
        return BuyInsertMoneyPage(self.driver)