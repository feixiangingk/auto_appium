#coding:utf-8
from functions.BasePage import BasePage
from selenium.webdriver.common.by import  By
from pages.register_identity_auth_page import RegisterIdentityAuthPage
from appium.webdriver.common.touch_action import TouchAction

class RegisterPatternlockPage(BasePage):
    context="register patternlock page"

    #整个图形锁按钮
    @property
    def el_Parttern_lock(self):
        return self.base_find_element(By.ID,"com.quarkfinance.ufo:id/sudoku")

    #跳转至register_identity_auth_page
    def logic_drawGestureCode(self):

        dic_size = self.el_Parttern_lock.size
        dic_loc =self.el_Parttern_lock.location
        step = dic_size['height'] / 4
        beginX = dic_loc['x'] + 2 * step
        beginY = dic_loc['y'] + 2 * step
        TouchAction(self.driver).press(x=beginX, y=beginY).wait(1000).move_to(x=step + 10, y=0).wait(1000).move_to(
            x=0, y=step).wait(1000).move_to(x=-step, y=0).wait(1000).move_to(x=-step, y=0).wait(
            1000).release().perform()

        TouchAction(self.driver).press(x=beginX, y=beginY).wait(1000).move_to(x=step + 10, y=0).wait(1000).move_to(
            x=0, y=step).wait(1000).move_to(x=-step, y=0).wait(1000).move_to(x=-step, y=0).wait(
            1000).release().perform()

        return RegisterIdentityAuthPage(self.driver)

