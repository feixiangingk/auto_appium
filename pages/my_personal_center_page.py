#coding:utf-8

import time,sys
reload(sys)
sys.setdefaultencoding('utf-8')

from functions.BasePage import BasePage
from selenium.webdriver.common.by import By
from functions.appium_init import *
from pages.banner_pages import BannerPages
from pages.home_page import HomePage
from pages.my_modify_password_page import Modify_Password_page
from appium.webdriver.common.touch_action import TouchAction



class MyPersonalCenterPage(BasePage):
    """个人中心"""

    context='my personal center page'

    #手机号文本 元素
    @property
    def el_phone_text(self):
        return self.base_find_element(By.ID,"com.quarkfinance.ufo:id/tv_phonenumber")

    #姓名
    @property
    def el_username_text(self):
        return self.base_find_element(By.ID,"com.quarkfinance.ufo:id/tv_username")

     #身份证号
    @property
    def el_ID_text(self):
        return self.base_find_element(By.ID, "com.quarkfinance.ufo:id/tv_shenfenzheng")


    #退出登录
    @property
    def el_login_out_btn(self):
        return self.base_find_element(By.ID, "com.quarkfinance.ufo:id/tv_login_out")

    #修改密码
    @property
    def el_modify_password_btn(self):
        return self.base_find_element(By.ID,"com.quarkfinance.ufo:id/re_amend_pass")

    # 修改手势密码
    @property
    def el_gesture_cipher_btn(self):
        return self.base_find_element(By.ID, "com.quarkfinance.ufo:id/re_amend_gest_pass")



    #获取个人信息
    def logic_get_user_information(self):
        phonenum=self.el_phone_text.text
        username=self.el_username_text.text
        ID=self.el_ID_text.text
        user_information={"phonenum":phonenum,"username":username,"ID":ID}

        return  user_information


    #退出登录
    def logic_login_out_btn_click(self):
        self.el_login_out_btn.click()
        return HomePage(self.driver)


    #修改密码

    def logic_modify_password_btn_click(self):
        self.el_modify_password_btn.click()
        return Modify_Password_page(self.driver)


    # 整个图形锁按钮
    @property
    def el_Parttern_lock(self):
        return self.base_find_element(By.ID, "com.quarkfinance.ufo:id/sudoku")


    def logic_drawGestureCode(self):

        dic_size = self.el_Parttern_lock.size
        dic_loc =self.el_Parttern_lock.location
        step = dic_size['height'] / 4
        beginX = dic_loc['x'] + 2 * step
        beginY = dic_loc['y'] + 2 * step
        TouchAction(self.driver).press(x=beginX, y=beginY).wait(1000).move_to(x=step + 10, y=0).wait(1000).move_to(
            x=0, y=step).wait(1000).move_to(x=-step, y=0).wait(1000).move_to(x=-step, y=0).wait(
            1000).release().perform()
        time.sleep(0.5)

        TouchAction(self.driver).press(x=beginX, y=beginY).wait(1000).move_to(x=step + 10, y=0).wait(1000).move_to(
            x=0, y=step).wait(1000).move_to(x=-step, y=0).wait(1000).move_to(x=-step, y=0).wait(
            1000).release().perform()
        time.sleep(0.5)
        TouchAction(self.driver).press(x=beginX, y=beginY).wait(1000).move_to(x=step + 10, y=0).wait(1000).move_to(
            x=0, y=step).wait(1000).move_to(x=-step, y=0).wait(1000).move_to(x=-step, y=0).wait(
            1000).release().perform()

      #  return RegisterIdentityAuthPage(self.driver)


