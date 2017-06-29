#coding:utf-8
from functions.BasePage import BasePage
from appium.webdriver.common.touch_action import TouchAction
from pages.home_page import HomePage
import  time

class StartupPage(BasePage):


 # @staticmethod 这里作为静态方法，没必要，因为所有page都继承basePage,都有self属性，basePage自带driver
    def page_swipe(self):
        time.sleep(2)
        # BasePage(self.driver).swipe_to_right()
        self.swipe_to_right()
        time.sleep(2)
        self.swipe_to_right()
        # BasePage(self.driver).swipe_to_right()
        time.sleep(2)
        self.swipe_to_right()
        # BasePage(self.driver).swipe_to_right()
        time.sleep(2)
        self.press_TouchAction()
        # BasePage(self.driver).press_TouchAction()
        time.sleep(3)
        return HomePage(self.driver)

