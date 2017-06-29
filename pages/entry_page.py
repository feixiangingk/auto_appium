#coding:utf-8
from pages.my_page import MyPage
from functions.BasePage import BasePage
from selenium.webdriver.common.by import By
from pages.banner_pages import BannerPages
from functions.appium_init import *
from pages.product_list_page import ProductListPage
from pages.news_page import NewsPage
from pages.my_invset_record_page import MyInvsetRecorePage
from pages.startup_page import StartupPage
from pages.my_page import MyPage
import time,sys
reload(sys)
sys.setdefaultencoding('utf-8')


class Entry_page(BasePage):
    """
        启动入口paga,将APP中所有page入口整合在一起
    """

    """
    open_start_home_page  首次启动APP首页
    open_login_page  登录页
    open_login_home_page 登录状态首页
    open_login_my_page  登录状态个人信息页
    open_my_assetDetails_page 资产详情
    
    """


    def open_start_home_page(self):
        startupPage = StartupPage(self.driver)
        homepage = startupPage.page_swipe()
        return homepage


    def open_login_page(self):
        homepage=self.open_start_home_page()
        loginPage=homepage.logic_link_login_page()
        return loginPage

    def open_forget_pass_page(self):
        loginPage=self.open_login_page()
        forget_Pass=loginPage.logic_el_forget_pass_click()
        return  forget_Pass



    # 登录状态返回homepage
    def open_login_home_page(self):
        loginPage=self.open_login_page()
        homepage = loginPage.logic_login(self.phone,self.pwd)
        return homepage



    def open_login_my_page(self):
        homepage=self.open_login_home_page()
        mypage = homepage.click_el_my_btn()
        time.sleep(0.1)
        mypage.el_tv_know.click()
        return mypage

    #个人中心
    def open_my_Personal_CenterPage(self):
        mypage=self.open_login_my_page()
        myPersonalCenterPage=mypage.logic_link_myCenter()
        return  myPersonalCenterPage



    #登录状态进去产品列表
    def open_login_productList_page(self):
        homepage = self.open_login_home_page()
        productListPage=homepage.logic_link_product()
        return  productListPage




        #登录状态进入投资记录页面
    def open_my_invset_recore_Page(self):
        mypage=self.open_login_my_page()
        myinvsetrecorepage = mypage.click_my_investmentRecord()
        myinvsetrecorepage.el_tv_know.click()
        return myinvsetrecorepage




        #登录状态，理财中资产详情
    def open_my_assetDetails_page(self):
        myinvsetrecorepage=self.open_my_invset_recore_Page()
        myAssetDetailsPage=myinvsetrecorepage.logic_invest_list_click()
        return myAssetDetailsPage

    # 登录状态，退出中资产详情
    def open_my_assetDetails_quiting_page(self):
        myinvsetrecorepage = self.open_my_invset_recore_Page()
        myinvsetrecorepage.el_drop_out_btn.click()
        time.sleep(1.5)
        myAssetDetailsPage = myinvsetrecorepage.logic_invest_list_click()
        return myAssetDetailsPage

    #登录状态，已退出资产详情
    def open_my_assetDetails_Exited_page(self):
        myinvsetrecorepage = self.open_my_invset_recore_Page()
        myinvsetrecorepage.el_exited_btn.click()
        time.sleep(1.5)
        myAssetDetailsPage = myinvsetrecorepage.logic_invest_list_click()
        return myAssetDetailsPage


        #登录状态，理财中资产详情合同页面
    def open_Electronic_contract_page(self):
        myAssetDetailsPage=self.open_my_assetDetails_page()
        time.sleep(1)
        electronic_contract_page=myAssetDetailsPage.click_pact()
        return  electronic_contract_page


    #登录状态进入交易记录页面
    def open_my_tradeRecord_page(self):
        mypage=self.open_login_my_page()
        mytradeRecordPage=mypage.logic_my_transactionRecord_btn_click()
        return mytradeRecordPage

    def open_news_page(self):
        homepage=self.open_login_home_page()
        newsPage=homepage.logic_click_el_news_img()
        return newsPage

    #修改密码
    def open_Modify_Password_page(self):
        myPersonalCenterPage=self.open_my_Personal_CenterPage()
        Modify_Password_page=myPersonalCenterPage.logic_modify_password_btn_click()
        return  Modify_Password_page


    #登录状态_产品列表

    #登录状态私募预约
    def open_Private_Offering_Fund_Page(self):
        homepage=self.open_login_home_page()
        productListPage=homepage.logic_link_login_product()

        private_Offering_Fund_Page=productListPage.logic_login_private_fund()
        return private_Offering_Fund_Page






