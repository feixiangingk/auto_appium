#coding=utf-8

import unittest,sys
sys.path.append('..')
import time
from functions.interface_case import InterfaceCase
from pages.startup_page import StartupPage
from functions.sqlServerJDBC import Exce_SQLserver
from functions.appium_init import *
from pages.my_invset_record_page import MyAssetDetailsPage
from pages.entry_page import Entry_page

class Personal_Center(InterfaceCase):
    """个人中心模块验证"""

    def setUp(self):
        self.driver = self.inital.get_driver()
        self.logger = self.inital.logger


    def test_user_Information(self):
        """个人中心-个人信息验证"""
        entry_page=Entry_page(self.driver,phone="18048444414",pwd='qwe123')
        myPersonalCenterPage=entry_page.open_my_Personal_CenterPage()

        user_information=myPersonalCenterPage.logic_get_user_information()

        sql = Exce_SQLserver()
        sql_user_information = sql.execSql_getList("SELECT Name,new_telephone1,new_certificatenum from AccountBase  WHERE new_telephone1={phone}".format(phone=entry_page.phone))

        ""
        [('username', u'u***1'), ('phonenum', u'144****8098'), ('ID', u'411***********3286')]
        [(u'14488888098', u'ufo21', 411224197404103286)]
        ""
        username=sql_user_information[0][0]
        phonenum=sql_user_information[0][1]
        ID=sql_user_information[0][2]

        entry_page.saveScreenshot('user_Information')
        #断言
        self.assertEquals(user_information["username"],username[:1]+'*'+username[-1:])
        self.assertEquals(user_information["phonenum"],phonenum[:3]+'****'+phonenum[-4:])
        self.assertEquals(user_information["ID"], ID[:3] + '***********' + ID[-4:])


    def test_login_out(self):
        """个人中心-安全退出测试"""
        entry_page = Entry_page(self.driver, phone="18048444414", pwd='qwe123')
        myPersonalCenterPage = entry_page.open_my_Personal_CenterPage()
        homepage=myPersonalCenterPage.logic_login_out_btn_click()

        entry_page.saveScreenshot('login_out')
        product_name=homepage.get_product_title_text()
        self.assertEquals(product_name,"新手体验计划")



    def test_modify_password(self):
        """个人中心-修改登录密码测试"""
        entry_page = Entry_page(self.driver, phone="18048444414", pwd='qwe123')
        modify_password_page = entry_page.open_Modify_Password_page()
        modify_password_page.el_current_pass_text.send_keys(entry_page.pwd)
        modify_password_page.el_password_text.send_keys("hele5201")
        modify_password_page.el_reinput_pass_text.send_keys("hele5201")
        loginPage=modify_password_page.logic_nextstep_btn_click()

        homePage=loginPage.logic_login(phone="18048444414", pwd='hele5201')
        mypage=homePage.logic_buy_my_btn()
        myPersonalCenterPage=mypage.logic_link_myCenter()
        modify_Password_page=myPersonalCenterPage.logic_modify_password_btn_click()

        modify_Password_page.el_current_pass_text.send_keys('hele5201')
        modify_Password_page.el_password_text.send_keys("qwe123")
        modify_Password_page.el_reinput_pass_text.send_keys("qwe123")
        modify_Password_page.logic_nextstep_btn_click()
        entry_page.saveScreenshot('modify_password')


    def test_gesture_cipher(self):
        """个人中心-修改手势密码"""
        entry_page = Entry_page(self.driver, phone="18048444414", pwd='qwe123')
        myPersonalCenterPage=entry_page.open_my_Personal_CenterPage()
        myPersonalCenterPage.el_gesture_cipher_btn.click()
        myPersonalCenterPage.logic_drawGestureCode()
        time.sleep(1)
        entry_page.saveScreenshot('gesture_cipher')


    def tearDown(self):
        self.driver.quit()






if __name__ == '__main__':
        Init()
        unittest.main(verbosity=2)
