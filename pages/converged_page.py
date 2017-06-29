#coding:utf-8
from functions.BasePage import BasePage
from pages.startup_page import StartupPage
from functions.random_data import Create_Data
from functions.appium_init import *
import  time

class ConvergedPage(BasePage):


    def register_customer(self):
        user_phone=Create_Data().get_phone()
        user_name=Create_Data().get_name()
        user_id=Create_Data.get_identification()
        user_email=Create_Data.get_random_mail()
        user_card=Create_Data.get_bank_card_zg()
        user_pwd='123456q'
        bankType="ZG"

        # user_phone='14488888083'
        # user_name='ufo83'
        # user_id=Create_Data.get_identification()
        # user_email=Create_Data.get_random_mail()
        # user_card=Create_Data.get_bank_card_js()
        # user_pwd='123456q'


        startupPage = StartupPage(self.driver)
        homePage = startupPage.page_swipe()
        loginPage = homePage.logic_link_login_page()
        registerChoosePage = loginPage.logic_link_register()
        registerSmsPage = registerChoosePage.logic_link_new_user()
        registerPasswordPage = registerSmsPage.logic_entry_info(user_phone)
        registerReferencePage = registerPasswordPage.logic_entry_pwd()
        registerPatternlockPage = registerReferencePage.logic_link_hulue()
        registerIdentityAuthPage = registerPatternlockPage.logic_drawGestureCode()
        homePage = registerIdentityAuthPage.logic_entry_user_info(user_name, user_id, user_email)

        homePage.el_my_btn.click()
        myPage=homePage.click_el_my_btn()

        #点击浮层
        myPage.el_tv_know.click()
        myBankCardPage=myPage.logic_my_bankCard_click()
        registerAddCardPage=myBankCardPage.logic_addCard_click()
        myBankCardPage=registerAddCardPage.logic_insert_bankCard_INFO(user_name,user_phone,user_card,bankType)
        self.driver.quit()
        appium_init.inital.logger.info('ConvergedPage: userName={one};phone={two};pwd={three};identification={four};bankType={five};cardNo={six}'.format(one=user_name,two=user_phone,three=user_pwd,four=user_id,five=bankType,six=user_card))
        return (user_phone,user_pwd)


    def register_bankcard(self,bankType):
        user_phone=Create_Data().get_phone()
        user_name=Create_Data().get_name()
        user_id=Create_Data.get_identification()
        user_email=Create_Data.get_random_mail()
        user_card=Create_Data.get_bank_card_js()
        user_pwd='123456q'
        # bankType="ZX"

        startupPage = StartupPage(self.driver)
        homePage = startupPage.page_swipe()
        loginPage = homePage.logic_link_login_page()
        registerChoosePage = loginPage.logic_link_register()
        registerSmsPage = registerChoosePage.logic_link_new_user()
        registerPasswordPage = registerSmsPage.logic_entry_info(user_phone)
        registerReferencePage = registerPasswordPage.logic_entry_pwd()
        registerPatternlockPage = registerReferencePage.logic_link_hulue()
        registerIdentityAuthPage = registerPatternlockPage.logic_drawGestureCode()
        homePage = registerIdentityAuthPage.logic_entry_user_info(user_name, user_id, user_email)

        homePage.el_my_btn.click()
        myPage=homePage.click_el_my_btn()

        #点击浮层
        myPage.el_tv_know.click()
        myBankCardPage=myPage.logic_my_bankCard_click()
        registerAddCardPage=myBankCardPage.logic_addCard_click()
        myBankCardPage=registerAddCardPage.logic_insert_bankCard_INFO(user_name,user_phone,user_card,bankType)
        appium_init.inital.logger.info('ConvergedPage: userName={one};phone={two};pwd={three};identification={four};bankType={five};cardNo={six}'.format(one=user_name,two=user_phone,three=user_pwd,four=user_id,five=bankType,six=user_card))
        return myBankCardPage,user_card