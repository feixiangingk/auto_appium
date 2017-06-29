#coding:utf-8
import unittest,sys
sys.path.append("..")
from functions.interface_case import InterfaceCase
from functions.appium_init import *
from pages.startup_page import StartupPage
from pages.home_page import HomePage
from functions.random_data import Create_Data
from functions.BasePage import BasePage

class RegisterTest(InterfaceCase):
    '''注册相关测试用例集'''

    def setUp(self):
        self.driver=self.inital.get_driver()
        self.logger=self.inital.logger

    def test_new_customer(self):
        '''注册新客户，并在我的个人中心，根据手机号断言'''
        user_phone=Create_Data().get_phone()
        user_name=Create_Data().get_name()
        user_id=Create_Data.get_identification()
        user_email=Create_Data.get_random_mail()

        startupPage=StartupPage(self.driver)
        homePage=startupPage.page_swipe()
        loginPage=homePage.logic_link_login_page()
        registerChoosePage=loginPage.logic_link_register()
        registerSmsPage=registerChoosePage.logic_link_new_user()
        registerPasswordPage=registerSmsPage.logic_entry_info(user_phone)
        registerReferencePage=registerPasswordPage.logic_entry_pwd()
        registerPatternlockPage=registerReferencePage.logic_link_hulue()
        registerIdentityAuthPage=registerPatternlockPage.logic_drawGestureCode()
        homePage=registerIdentityAuthPage.logic_entry_user_info(user_name,user_id,user_email)

        homePage.el_my_btn.click()
        myPage=homePage.click_el_my_btn()

        #点击浮层
        myPage.el_tv_know.click()

        #断言代码
        myPersonalCenterPage=myPage.logic_link_myCenter()
        phone_text=myPersonalCenterPage.el_phone_text.text
        phone_secret=user_phone[:3]+'****'+user_phone[7:]

        self.basepage = BasePage(self.driver)
        self.basepage.saveScreenshot('new_customer')
        self.assertEqual(phone_text,phone_secret)
        self.logger.info("userinfo:phone-{phone} name-{name} id-{id} email-{email}".format(phone=user_phone,name=user_name,
                                                                id=user_id,email=user_email))
    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
    Init()
    unittest.main()