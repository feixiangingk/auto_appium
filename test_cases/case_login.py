#coding:utf-8
import unittest,sys
sys.path.append('..')
from functions.appium_init import *
from functions.interface_case import InterfaceCase
from pages.startup_page import StartupPage
from functions.BasePage import BasePage
from pages.entry_page import Entry_page
from functions.sms_verification import Message
from functions.sqlServerJDBC import Exce_SQLserver


class LoginTest(InterfaceCase):
    '''登录模块验证'''

    def setUp(self):
        self.driver=self.inital.get_driver()
        self.logger=self.inital.logger

    #@unittest.skip('skip')
    def test_non_login_state_clickBuy(self):
        '''非登录态点击“立即投资”按钮测试用例'''
        startupPage=StartupPage(self.driver)
        homePage=startupPage.page_swipe()
        productListPage=homePage.logic_link_product()
        productQuarkzxPage=productListPage.logic_link_quarkZX()
        loginPage=productQuarkzxPage.logic_noLogin_state_buy()

        self.basepage = BasePage(self.driver)
        self.basepage.saveScreenshot('non_login_state_clickBuy')
        self.logger.info("run case:case_login.test_non_login_state_clickBuy")
        self.assertTrue(loginPage.element_is_exsit(loginPage.el_phone_text_input))

    #@unittest.skip('skip')
    def test_non_login_state_calculation(self):
        '''非登录状态点击理财计算器测试用例'''
        startupPage=StartupPage(self.driver)
        homePage=startupPage.page_swipe()
        productListPage=homePage.logic_link_product()
        productQuarkzxPage=productListPage.logic_link_quarkZX()
        productCalculationPage=productQuarkzxPage.logic_link_calculation_Page()
        page_title=productCalculationPage.el_title.text
        productCalculationPage.saveScreenshot('test_non_login_state_calculation')
        self.logger.info("run case:case_login.test_non_login_state_calculation")
        self.assertEqual(page_title,'理财计算器')

    #@unittest.skip("2")
    def test_non_login_state_clickFund(self):
        '''非登录状态点击基金列表'''
        startupPage = StartupPage(self.driver)
        homePage = startupPage.page_swipe()
        productListPage=homePage.logic_link_product()
        loginPage=productListPage.logic_nologin_state_fund()
        page_title=loginPage.el_title.text
        loginPage.saveScreenshot('test_non_login_state_clickFund')
        self.logger.info("run case:case_login.test_non_login_state_clickFund")
        self.assertEqual(page_title,u'登录')

    #@unittest.skip("2")
    def test_non_login_state_clickReinvsetment(self):
        '''非登录状态点击续投列表'''
        startupPage = StartupPage(self.driver)
        homePage = startupPage.page_swipe()
        productListPage = homePage.logic_link_product()
        loginPage = productListPage.logic_nologin_state_reinvestment()

        page_title = loginPage.el_title.text
        loginPage.saveScreenshot('test_non_login_state_clickFund')
        self.logger.info("run case:case_login.test_non_login_state_clickReinvsetment")
        self.assertEqual(page_title, u'登录')

    #@unittest.skip('skip')
    def test_non_login_state_clickMyPage(self):
        '''非登录状态点击“我的”按钮测试用例'''
        startupPage=StartupPage(self.driver)
        homePage=startupPage.page_swipe()
        loginPage=homePage.logic_link_login_page()

        self.basepage = BasePage(self.driver)
        self.basepage.saveScreenshot('non_login_state_clickMyPage')
        self.logger.info("run case:case_login.test_non_login_state_clickMyPage")
        self.assertTrue(loginPage.element_is_exsit(loginPage.el_pwd_text_input))

    #@unittest.skip('skip')
    def test_login_success(self):
        '''登录成功测试用例'''
        user_phone='14488888098'
        pwd='qwe123'

        startupPage=StartupPage(self.driver)
        homePage=startupPage.page_swipe()
        loginPage=homePage.logic_link_login_page()
        homePage=loginPage.logic_login(user_phone,pwd)

        myPage=homePage.click_el_my_btn()
        # 点击浮层
        time.sleep(1)
        myPage.el_tv_know.click()
        # 断言代码
        myPersonalCenterPage = myPage.logic_link_myCenter()
        phone_text = myPersonalCenterPage.el_phone_text.text
        phone_secret = user_phone[:3] + '****' + user_phone[7:]

        self.basepage = BasePage(self.driver)
        self.basepage.saveScreenshot('login_success')
        self.logger.info("run case:case_login.test_login_success")
        self.assertEqual(phone_text, phone_secret)

    def test_Forgot_password(self):
        """找回密码验证"""
        entry_page=Entry_page(self.driver)
        forget_Pass=entry_page.open_forget_pass_page()
        forget_Pass.el_edit_phone.send_keys(entry_page.phone)
        forget_Pass.el_get_verify.click()
        message=Message()
        yanzma=message.get_sms(entry_page.phone)
        forget_Pass.el_edit_yanzheng.send_keys(yanzma)
        forget_Pass.el_tv_nextstepself.click()

        sql = Exce_SQLserver()
        contract_number = sql.execSql_getList("SELECT Name,new_certificatenum FROM AccountBase WHERE  new_telephone1={phone}".format(phone=entry_page.phone))
        forget_Pass.el_edit_phone.send_keys(contract_number[0][0])
        forget_Pass.el_edit_yanzheng.send_keys(contract_number[0][1])
        forget_Pass.el_tv_nextstepself.click()
        forget_Pass.el_edit_password.send_keys("qwe1234")
        forget_Pass.el_edit_reinput.send_keys("qwe1234")
        loginPage=forget_Pass.logic_tv_nextstepself_click()
        #loginPage=homePage.logic_buy_my_btn()


        forget_Pass=loginPage.logic_el_forget_pass_click()
        forget_Pass.el_edit_phone.send_keys(entry_page.phone)
        forget_Pass.el_get_verify.click()
        message = Message()
        yanzma = message.get_sms(entry_page.phone)
        forget_Pass.el_edit_yanzheng.send_keys(yanzma)
        forget_Pass.el_tv_nextstepself.click()

        #sql = Exce_SQLserver()
       # contract_number = sql.execSql_getList("SELECT Name,new_certificatenum FROM AccountBase WHERE  new_telephone1={phone}".format(phone=entry_page.phone))
        forget_Pass.el_edit_phone.send_keys(contract_number[0][0])
        forget_Pass.el_edit_yanzheng.send_keys(contract_number[0][1])
        forget_Pass.el_tv_nextstepself.click()
        forget_Pass.el_edit_password.send_keys("qwe123")
        forget_Pass.el_edit_reinput.send_keys("qwe123")
        self.assertEquals(forget_Pass.el_tb_title.text,'找回密码')
        forget_Pass.el_tv_nextstepself.click()

        entry_page.saveScreenshot("Forgot_password")


    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    Init()
    unittest.main()


